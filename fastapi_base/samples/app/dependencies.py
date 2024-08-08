"""
FastAPI dependencies for the app {app_name}
"""

<<<<<<< HEAD
from core.{app_name}.service import YourModelRepository, YourModelService 
=======
from src.{app_name}.service import {table_name}Repository, {table_name}Service 
>>>>>>> ee1a26888708d55deb24fe098c9e68df619a526d

# TODO: define your dependencies here
def get_{app_name}_service():
    return {table_name}Service({table_name}Repository)