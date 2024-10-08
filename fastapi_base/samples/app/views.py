from fastapi import APIRouter, status, Depends

from api.{app_name}.config import (
    PREFIX,
    TAGS,
    INCLUDE_IN_SCHEMA
)
from api.{app_name}.dependencies import get_{app_name}_service
from api.{app_name}.service import {table_name}Service
from api.{app_name}.schemas import {table_name}CreateSchema, {table_name}GetSchema, {table_name}UpdateSchema


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS,
    include_in_schema=INCLUDE_IN_SCHEMA
)


@router.get('/{{id}}', response_model={table_name}GetSchema, status_code=status.HTTP_200_OK)
async def get_one(
    id: int,
    service: {table_name}Service = Depends(get_{app_name}_service),
):
    item = await service.get_by_id(id)
    return item


@router.post('/', response_model={table_name}GetSchema, status_code=status.HTTP_201_CREATED)
async def create_one(
    item: {table_name}CreateSchema,
    service: {table_name}Service = Depends(get_{app_name}_service),
):
    new_item = await service.create(item)
    return new_item


@router.put('/{{id}}', response_model={table_name}GetSchema, status_code=status.HTTP_200_OK)
async def update_one(
    id: int,
    new_item: {table_name}CreateSchema,
    service: {table_name}Service = Depends(get_{app_name}_service),
):
    new_item = await service.update(id, new_item)
    return new_item


@router.delete('/{{id}}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    id: int,
    service: {table_name}Service = Depends(get_{app_name}_service),
):
    await service.delete(id)


@router.get('/', status_code=status.HTTP_200_OK)
async def get_all(
    limit: int = 10,
    offset: int = 0,
    service: {table_name}Service = Depends(get_{app_name}_service),
):
    items = await service.get_all(limit=limit, offset=offset)
    return items