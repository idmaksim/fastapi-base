from fastapi_base.app import App
from fastapi_base.schema_generator import SchemaGenerator
import os


class CRUDApp:
    def __init__(self, name: str, json_path: str) -> None:
        self.name = name
        self.json_path = json_path 
        
        self.create_app()
        self.create_models()
        
    def create_app(self) -> None:
        app = App(self.name)
        app.create_files()

    def create_models(self) -> None:
        schema_generator = SchemaGenerator()
        schema_generator.gen_from_json(SchemaGenerator.Model.Pydantic, self.json_path, os.path.join(self.name, 'schemas.py'))
        schema_generator.gen_from_json(SchemaGenerator.Model.SQLAlchemy, self.json_path, os.path.join(self.name, 'models.py'))