from api.{app_name}.service import {table_name}Repository, {table_name}Service 


def get_{app_name}_service():
    return {table_name}Service({table_name}Repository)