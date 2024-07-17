"""
Views controllers for {app_name} app
"""


from fastapi import APIRouter, status, Depends

from src.{app_name}.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)

from src.{app_name}.dependencies import get_{app_name}_service
from src.{app_name}.service import YourModelService
from src.{app_name}.schemas import YourModelCreateSchema, YourModelGetSchema, YourModelUpdateSchema


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA
)


@router.get('/', response_model=YourModelGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
    id: int,
    service: YourModelService = Depends(get_{app_name}_service),
):
    ...


@router.post('/', response_model=YourModelGetSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    item: YourModelCreateSchema,
    service: YourModelService = Depends(get_{app_name}_service),
):
    ...


@router.put('/', response_model=YourModelGetSchema, status_code=status.HTTP_200_OK)
async def update_one(
    id: int,
    new_item: YourModelUpdateSchema,
    service: YourModelService = Depends(get_{app_name}_service),
):
    ...


@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    id: int,
    service: YourModelService = Depends(get_{app_name}_service),
):
    ...


@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    service: YourModelService = Depends(get_{app_name}_service),
):
    ...