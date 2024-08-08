import json
from typing import Dict, List, Set, Optional
from enum import Enum 


class SchemaGenerator:     
    class Model(Enum):
        Pydantic: str = 'pydantic'
        SQLAlchemy: str = 'sqlalchemy'
        
    def gen_from_json(self, model_type: Model, input_path: str, output_path: str):
        with open(input_path, 'r') as json_file:
            schema = json.load(json_file)
            
        model = self.generate_model(schema, model_type) 
    
        self.write_model(model, model_type, output_path)
        
    def generate_model(self, schema: Dict, model_type: Model, model_name: str = None):
        # nested_models = []
        properties = schema.get("properties", [])
        fields: List[Set] = []
        
        for prop, details in properties.items():
            # if details["type"] == "object": # handle json
            #     nested_model = properties.get(prop)
            #     nested_models.append(self.generate_model(nested_model, model_type, prop.capitalize()))
            #     fields.append((prop, prop.capitalize()))
            if details["type"] == "array" and details["items"].get("type") is not None:
                field_type = self.get_field_mappings(details["type"], model_type, details["items"]["type"])
                fields.append((prop, field_type))
            else:
                field_type =  self.get_field_mappings(details["type"], model_type)
                fields.append((prop, field_type))
                
        class_name = schema.get("title") or model_name
        required_fields = schema.get("required", [])
        
        model = {
            "class_name": class_name,
            "fields": fields,
            "required_fields": required_fields,
            # "nested_models": nested_models
        }

        return model
    
    def write_model(self, model: Dict, model_type: Model, output_path: str):
        pydantic_imports: List[str] = [
            "from pydantic import BaseModel",
            "from typing import List, Dict, Set, Optional",
            "from datetime import datetime"
        ]
        
        sqlalchemy_imports: List[str] = [
            "from sqlalchemy import Column, Integer, Boolean, String, UUID, Float, ARRAY, DateTime",
            "from uuid import uuid4",
            "from src.database import Base"
        ]
        
        with open(output_path, 'w') as file:
            imports = pydantic_imports if model_type is self.Model.Pydantic else sqlalchemy_imports
            for import_line in imports:
                file.write(import_line + '\n')
            file.write("\n\n")
            
            pydantic_is_id, pydantic_is_uuid = False, False
            
            sup_class: str = "BaseModel" if model_type is self.Model.Pydantic else "Base" 
            model_name = model['class_name'] if model_type is self.Model.SQLAlchemy else f"{model['class_name']}CreateSchema"
            file.write(f"class {model_name}({sup_class}):\n")
            for name, type in model["fields"]:
                if name in model["required_fields"]:
                    is_id, is_uuid = False, False
                    if name.lower() == "id":
                        is_id = True
                        if model_type == self.Model.Pydantic:
                            pydantic_is_id = True
                            continue
                    elif name.lower() == "uuid":
                        is_uuid = True
                        if model_type == self.Model.Pydantic:
                            pydantic_is_uuid = True 
                            continue
                        
                    file.write(f"\t{name}: {type}"  if model_type is self.Model.Pydantic  
                                else f"\t{name} = Column({type}, primary_key=True, default=uuid4)" if is_uuid
                                else f"\t{name} = Column({type}, primary_key=True)" if is_id
                                else f"\t{name} = Column({type}, nullable=False)" )
                else:
                    file.write(f"\t{name}: Optional[{type}]" if model_type is self.Model.Pydantic
                                else f"\t{name} = Column({type}, nullable=True)")
                file.write('\n')
            file.write("\n\n")
            
            
            if pydantic_is_uuid or pydantic_is_id:
                file.write(f"class {model['class_name']}GetSchema(BaseModel):\n")
                file.write("\tid: int" if pydantic_is_id
                            else "\tuuid: UUID")
                file.write("\n")
        

    def get_field_mappings(self, json_type: str, model_type: Model,  items_type: Optional[str] = None):
        field_mapping_pydantic = {
            "uuid": "UUID",
            "string": "str",
            "number": "float",
            "integer": "int",
            "boolean": "bool",
            "array": f"List[{self.get_field_mappings(items_type, model_type)}]" if items_type else "List" ,
            "object": "Dict[str, Any]",
            "datetime": "datetime",
            "null": "None"
        }
        
        field_mapping_sqlalchemy = {
            "uuid": "UUID",
            "string": "String",
            "number": "Float",
            "integer": "Integer",
            "boolean": "Boolean",
            "array": f"ARRAY({self.get_field_mappings(items_type, model_type)})" if items_type else "Array",
            "datetime": "DateTime"
        }
        
        return field_mapping_pydantic.get(json_type) if model_type == self.Model.Pydantic else field_mapping_sqlalchemy.get(json_type)
    