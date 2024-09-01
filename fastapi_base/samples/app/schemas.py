from pydantic import BaseModel


class {table_name}CreateSchema(BaseModel):
    ...


class {table_name}GetSchema({table_name}CreateSchema):
    ...
