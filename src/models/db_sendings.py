from ._engine import async_session
from ._models import User

from datetime import timedelta, datetime
from sqlalchemy.sql.expression import select, update, func, or_


async def get_users_autosending_1() -> list[int]:
    async with async_session() as session: 
        query = select(User.id).filter(User.got_autosending_1.isnot(None),
                                    (func.now() - User.got_autosending_1) >= timedelta(minutes=10))
        result = await session.execute(query)
        return result.scalars().all()


async def mark_got_autosending_1(id_):
    """
    Present after webinar information
    """

    query = update(User).values(got_autosending_1=func.now()).where(User.id == id_)
    async with async_session() as session:
        await session.execute(query)
        await session.commit()


async def get_users_autosending_2():
    async with async_session() as session:  # TODO
        query = select(User).filter(User.got_autosending_2.isnot(None))
        result = await session.execute(query)
        return result.scalars().all()


async def mark_got_autosending_2(id_):
    """
    Present after registration
    """

    query = update(User).values(got_autosending_2=func.now()).where(User.id == id_)
    async with async_session() as session:
        await session.execute(query)
        await session.commit()


async def update_autosending_1(id_: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.id == id_).values(got_autosending_1=None))
        await session.commit()


async def update_autosending_2(id_: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.id == id_).values(got_autosending_2=None))
        await session.commit()
