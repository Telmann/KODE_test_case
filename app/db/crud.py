from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..models import pydantic_models as schemas
from . import sqlalchemy_models as models


async def create_user(db: AsyncSession, user: schemas.User):
    user = models.User(**user.model_dump())
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def create_note(db: AsyncSession, note: schemas.Note):
    note = models.Note(**note.model_dump())
    db.add(note)
    await db.commit()
    await db.refresh(note)
    return note


async def read_notes(db: AsyncSession, user_id: int):
    notes = await db.execute(
        select(models.Note).filter(models.Note.user_id == user_id))
    return notes.scalars().all()
