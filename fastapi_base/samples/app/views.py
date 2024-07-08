from fastapi import APIRouter
from {app_name}.config import (
    PREFIX,
    TAGS
)


router = APIRouter(
    prefix=PREFIX,
    tags=TAGS
)


@router.get('/', response_model=..., status_code=...)
async def get_one(
    # define your args here
):
    ...


@router.post('/', response_model=..., status_code=...)
async def create_one(
    # define your args here
):
    ...


@router.put('/', response_model=..., status_code=...)
async def update_one(
    # define your args here
):
    ...


@router.delete('/', response_model=..., status_code=...)
async def delete_one(
    # define your args here
):
    ...