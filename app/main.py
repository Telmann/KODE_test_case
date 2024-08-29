from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.ext.asyncio import AsyncSession

from .auth import create_access_token, get_user, get_current_user

from .ya_spell_check import text_check
from .db.db import get_db
from .db.crud import create_note, read_notes, create_user

from .models.pydantic_models import Note, User

app = FastAPI()


@app.post("/registration")
async def user_registration(user: User, db: AsyncSession = Depends(get_db)):
    new_user = await create_user(db=db, user=user)
    if new_user:
        return {"message": "New user added to the db!"}
    return {"message": "Sorry, try again!"}


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(),
                db: AsyncSession = Depends(get_db)):
    user = await get_user(db, form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong username or password!!!",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = await create_access_token(data={"sub": user.login})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/notes", response_model=Note)
async def post_note(content: str,
                    db: AsyncSession = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    user_id = current_user.id
    text_errors = await text_check(content)
    if text_errors:
        raise HTTPException(status_code=400,
                            detail={
                                "message": "В вашем тексте обнаружены ошибки!",
                                "errors": text_errors
                            })
    note = Note(content=content, user_id=user_id)
    return await create_note(db=db, note=note)


@app.get("/notes", response_model=list[Note])
async def get_notes(db: AsyncSession = Depends(get_db),
                    current_user: User = Depends(get_current_user)):
    notes = await read_notes(db=db, user_id=current_user.id)
    return notes
