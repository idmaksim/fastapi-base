"""
Views controllers for {app_name} app
"""


from fastapi import APIRouter, status, Depends

from core.{app_name}.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)

from core.{app_name}.dependencies import get_{app_name}_service
from core.{app_name}.service import YourModelService
from core.{app_name}.schemas import YourModelCreateSchema, YourModelGetSchema, YourModelUpdateSchema


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA
)


@router.get('/{{id}}', response_model=YourModelGetSchema, status_code=status.HTTP_200_OK)
async def get_one(
    id: int,
    service: YourModelService = Depends(get_{app_name}_service),
):
    item = await service.get_by_id(id)
    return item


@router.post('/', response_model=YourModelGetSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    item: YourModelCreateSchema,
    service: YourModelService = Depends(get_{app_name}_service),
):
    new_item = await service.create(item)
    return new_item


@router.put('/{{id}}', response_model=YourModelGetSchema, status_code=status.HTTP_200_OK)
async def update_one(
    id: int,
    new_item: YourModelUpdateSchema,
    service: YourModelService = Depends(get_{app_name}_service),
):
    new_item = await service.update(id, new_item)
    return new_item


@router.delete('/{{id}}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    id: int,
    service: YourModelService = Depends(get_{app_name}_service),
):
    await service.delete(id)


@router.get('/', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    service: YourModelService = Depends(get_{app_name}_service),
):
    items = await service.get_all(limit=limit, offset=offset)
    return items