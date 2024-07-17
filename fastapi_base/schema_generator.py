import json
from typing import Dict, List, Set, Optional


class SchemaGenerator:
    def __init__(self, input_path: str, output_path: str):
        self.input_path = input_path
        self.output_path = output_path
        
    def gen_from_json(self):
        with open(self.input_path, 'r') as json_file:
            schema = json.load(json_file)
            
        model = self.generate_model(schema)
        self.write_model(model, self.output_path)
        
    def generate_model(self, schema: Dict, model_name: str = None):
        nested_models = []
        properties = schema.get("properties", [])
        fields: List[Set] = []
        
        for prop, details in properties.items():
            if details["type"] == "object": # handle json
                nested_model = properties.get(prop)
                nested_models.append(self.get_field_mappings(nested_model, prop.capitalize()))
                fields.append((prop, prop.capitalize()))
            elif details["type"] == "array" and details["items"].get("type") is not None:
                field_type = self.get_field_mappings(details["type"], details["items"]["type"])
                fields.append((prop, field_type))
            else:
                field_type =  self.get_field_mappings(details["type"])
                fields.append((prop, field_type))
                
        class_name = schema.get("title") or model_name
        required_fields = schema.get("required", [])
        
        model = f"class {class_name}(BaseModel):\n"
        for name, type in fields:
            if name in required_fields:
                model += f"    {name}: {type}\n"
            else:
                model += f"    {name}: Optional[{type}]\n"
            
        for nested_model in nested_models:
            model = nested_model + "\n\n" + model
        
        return model
    
    def write_model(self, model: str, path: str):
        imports: List[str] = [
            "from pydantic import BaseModel",
            "from typing import List, Dict, Set, Optional"
        ]
        
        with open(path, 'w') as file:
            for import_line in imports:
                file.write(import_line + '\n')
            file.write("\n\n")
            file.write(model)

    def get_field_mappings(self, json_type: str, items_type: Optional[str] = None):
        field_mapping = {
            "uuid": "UUID",
            "string": "str",
            "number": "float",
            "integer": "int",
            "boolean": "bool",
            "array": f"List[{self.get_field_mappings(items_type)}]" if items_type else "List" ,
            "object": "Dict[str, Any]",
            "null": "None",
        }
        
        return field_mapping.get(json_type)
    