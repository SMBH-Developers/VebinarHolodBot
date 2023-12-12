from ._engine import async_session
from ._models import User

from datetime import timedelta, datetime
from sqlalchemy.sql.expression import select, update, func, or_


async def get_users_autosending_1():
    async with async_session() as session:  # TODO
        ...
        # users = (await session.execute(select(User.id).where())).scalars().all()
    return ...


async def mark_got_autosending_1(id_):
    query = update(User).values(autosending_1=func.now()).where(User.id == id_)
    async with async_session() as session:
        await session.execute(query)
        await session.commit()


async def get_users_autosending_2():
    async with async_session() as session:  # TODO
        ...
        # users = (await session.execute(select(User.id).where())).scalars().all()
    return ...


async def mark_got_autosending_2(id_):
    query = update(User).values(autosending_2=func.now()).where(User.id == id_)
    async with async_session() as session:
        await session.execute(query)
        await session.commit()
