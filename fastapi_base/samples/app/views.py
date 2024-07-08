from fastapi import APIRouter, status

from src.{app_name}.config import (
    PREFIX,
    TAGS
)


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS
)


@router.get('/', response_model=..., status_code=status.HTTP_200_OK)
async def get_one(
    # define your args here
):
    ...


@router.post('/', response_model=..., status_code=status.HTTP_201_CREATED)
async def create_one(
    # define your args here
):
    ...


@router.put('/', response_model=..., status_code=status.HTTP_200_OK)
async def update_one(
    # define your args here
):
    ...


@router.delete('/', response_model=..., status_code=status.HTTP_204_NO_CONTENT)
async def delete_one(
    # define your args here
):
    ...