from typing import Optional, Any
from uuid import UUID

from sqlalchemy import select, exc
from sqlalchemy.ext.asyncio import AsyncSession

from cryptosales.user.models import User


async def get_user_by_telegram_id(session: AsyncSession, telegram_id: int) -> Optional[Any | None]:
    result = await session.execute(select(User).filter_by(telegram_id=telegram_id))
    return result.scalar_one()


async def get_user_by_id(session: AsyncSession, id_: UUID) -> Optional[Any]:
    user = await session.get(User, id_)
    return user


async def create_user(session: AsyncSession, user: User) -> Optional[Any]:
    session.add(user)
    try:
        await session.commit()
    except exc.IntegrityError:
        await session.rollback()
        return None
    return user.id


async def get_or_create_user_by_telegram_id(session: AsyncSession, telegram_id: int) -> Optional[Any]:
    await create_user(session, User(telegram_id=telegram_id))
    return await get_user_by_telegram_id(session, telegram_id)
