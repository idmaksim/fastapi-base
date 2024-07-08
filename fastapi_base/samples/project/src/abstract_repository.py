from abc import ABC, abstractmethod

from sqlalchemy import delete, insert, select, and_
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
    
    
class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict):
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model)
            res = await session.execute(statement=stmt)
            await session.flush()
            await session.commit()
            return res.scalar_one()

    async def get_all(self, limit: int = 10):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.id <= limit)
            res = await session.execute(statement=stmt)
            return res.scalars().all()

    async def get_one_by_id(self, id: int):
        async with async_session_maker() as session:
            stmt = select(self.model).filter_by(id=id)
            res = await session.execute(statement=stmt)
            return res.scalar()

    async def get_one_by_data(self, **filters):
        async with async_session_maker() as session:
            stmt = select(self.model).where(
                and_(
                    *[
                        getattr(self.model, key) == value for key, value in filters.items()
                    ]
                )
            )
            res = await session.execute(stmt)
            return res.scalar()

    async def delete_one_by_id(self, id: int):
        async with async_session_maker() as session:
            stmt = delete(self.model).filter_by(id=id).returning(self.model)
            res = await session.execute(statement=stmt)
            await session.commit()
            return res.scalar()