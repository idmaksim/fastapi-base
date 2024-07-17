"""
{app_name} schemas
"""

from pydantic import BaseModel


# define your schemas here and rename< which already exists
# TODO: rename YourModel to name of your model with press F2 button on class name


class YourModelBaseSchema(BaseModel):
    ...


class YourModelCreateSchema(YourModelBaseSchema):
    ...


class YourModelGetSchema(YourModelBaseSchema):
    ...


class YourModelUpdateSchema(YourModelBaseSchema):
    ...
