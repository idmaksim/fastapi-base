"""
FastAPI dependencies for the app {app_name}
"""

from src.{app_name}.service import YourModelRepository, YourModelService 

# TODO: define your dependencies here
def get_{app_name}_service():
    return YourModelService(YourModelRepository)