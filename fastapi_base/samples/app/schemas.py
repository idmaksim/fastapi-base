from pydantic import BaseModel


# define your schemas here and rename< which already exists
class ItemBase(BaseModel):
    ...

class ItemCreate(ItemBase):
    ...

class ItemGet(ItemBase):
    ...

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
