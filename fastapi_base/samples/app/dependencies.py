"""
FastAPI dependencies for the app {app_name}
"""

from core.{app_name}.service import {table_name}RepositoryRepository, {table_name}ServiceService 

# TODO: define your dependencies here
def get_{app_name}_service():
    return {table_name}Service({table_name}Repository)