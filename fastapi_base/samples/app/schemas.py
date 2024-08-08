"""
{app_name} schemas
"""

from pydantic import BaseModel


# define your schemas here 


class {table_name}CreateSchema(BaseModel):
    ...


class {table_name}GetSchema({table_name}CreateSchema):
    ...
