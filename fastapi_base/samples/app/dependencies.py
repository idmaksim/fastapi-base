"""
FastAPI dependencies for the app {app_name}
"""

from src.{app_name}.service import {table_name}Repository, {table_name}Service 

# TODO: define your dependencies here
def get_{app_name}_service():
    return {table_name}Service({table_name}Repository)