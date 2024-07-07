from abc import ABC, abstractmethod

from sqlalchemy import delete, insert, select, and_
import sqlalchemy
from database import async_session_maker


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def get_all():
        raise NotImplementedError

    @abstractmethod
    async def get_one_by_id():
        raise NotImplementedError

    @abstractmethod
    async def get_one_by_data():
        raise NotImplementedError

    @abstractmethod
    async def delete_one_by_id():
        raise NotImplementedError