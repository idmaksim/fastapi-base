from sqlalchemy.exc import IntegrityError

from api.abstract_repository import SQLAlchemyRepository, AbstractRepository
from api.{app_name}.models import {table_name}
from api.exceptions import ConflictException, NotFoundException
from api.{app_name}.schemas import {table_name}CreateSchema


class {table_name}Repository(SQLAlchemyRepository):
    model = {table_name}


class {table_name}Service:
    def __init__(self, repository: AbstractRepository):
        self.repository: AbstractRepository = repository()

    async def create(self, item: {table_name}CreateSchema):
        item_dict = item.model_dump()
        try:
            return await self.repository.create(item_dict)
        except IntegrityError:
            raise ConflictException()

    async def get_all(self, limit: int, offset: int):
        if items := await self.repository.read_all(limit, offset):
            return items
        raise NotFoundException()

    async def get_by_id(self, id: int):
        if item := await self.repository.read_by_id(id):
            return item
        raise NotFoundException()

    async def update(self, id: int, item: {table_name}CreateSchema):
        item_dict = item.model_dump()
    
        if upd_item := await self.repository.update_by_id(id, item_dict):
            return upd_item
        raise NotFoundException()

    async def delete(self, id: int):
        if item := await self.repository.delete_by_id(id):
            return item
        raise NotFoundException()