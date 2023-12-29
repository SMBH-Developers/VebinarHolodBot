from ._engine import async_session
from ._models import User, Sending

from datetime import date
from datetime import timedelta
from datetime import datetime
from typing import List

from sqlalchemy.sql.expression import select, update, delete, case, text
from sqlalchemy import func, extract


async def registrate_if_not_exists(id_: int, name: str):
    async with async_session() as session:
        exists = (await session.execute(select(User.id).where(User.id == id_).limit(1))).one_or_none()
        if exists is None:
            user = User(id=id_, name=name, state="main")
            sending = Sending(id="main", user_id=id_)
            session.add(user)
            session.add(sending)
            await session.commit()


async def check_user(id_: int) -> bool:
    async with async_session() as session:
        exists = (await session.execute(select(User.id).where(User.id == id_).limit(1))).one_or_none()
        if exists:
            return True
        
        return False


async def update_sended(id_: int):
    async with async_session() as session:
        await session.execute(update(User).where(User.id == id_).values(newsletter_sended=True))
        await session.commit()


async def update_state(id_: int, state: str):
    async with async_session() as session:
        await session.execute(update(User).where(User.id == id_).values(state=state, state_updated_at=func.now()))
        await session.execute(update(Sending).where(Sending.user_id == id_).values(id=state))
        await session.commit()


async def update_sent_sendings(id_: int):
    async with async_session() as session:
        await session.execute(update(Sending).where(Sending.user_id == id_).values(sent_at=func.now()))
        await session.commit()
        

async def get_before_web(id_: int):
    async with async_session() as session:
        result = await session.execute(select(User.before_web).where(User.id == id_))
        
    return result.scalars().one()


async def set_before_web(id_: int, before_web: int):
    async with async_session() as session:
        await session.execute(update(User).values(before_web=before_web).where(User.id == id_))
        await session.commit()


async def the_next_day_users():
    sub_query = (func.now() - User.registration_date)
    async with async_session() as session:
        query = select(User.id).filter(extract("day", sub_query) == 1)
        result = await session.execute(query)

    return result.scalars().all()
# async def delete_user(id_: int):
#     query = delete(User).where(User.id == id_)

#     async with async_session() as session:
#         await session.execute(query)
#         await session.commit()


# async def get_count_all_users() -> int:
#     query = select(func.count('*')).select_from(User)
#     async with async_session() as session:
#         count = (await session.execute(query)).scalar_one()
#     return count


async def get_users() -> List[tuple[User.id, User.name]]:
    async with async_session() as session:
        res = await session.execute(select(User.id, User.name))

    return res.fetchall()


# async def users_for_today_count() -> int:
#     query = select(func.count('*')).select_from(User).where(func.DATE(User.registration_date) == date.today())
#     async with async_session() as session:
#         count = (await session.execute(query)).scalar_one()
#     return count

async def get_users_to_gift(expired_time: int) -> list:
    async with async_session() as session:
        query = select(User.id).where(User.status == "alive", User.state == "waiting_gift").filter((User.state_updated_at + timedelta(minutes=expired_time) <= func.now()))
        result = await session.execute(query)

    return result.scalars().all()


async def get_users_to_newsletter(expired_time: int) -> list:
    async with async_session() as session:
        query = select(User.id).where(User.status == "alive", User.newsletter_sended == False).filter((User.registration_date + timedelta(minutes=expired_time) <= func.now()))
        result = await session.execute(query)

    return result.scalars().all()
                                       