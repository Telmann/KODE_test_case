from datetime import datetime, timedelta
from jose import JWTError, jwt
from sqlalchemy import select
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from secrets import token_urlsafe

from .db import sqlalchemy_models as models
from .db.db import get_db
from .models.pydantic_models import TokenData

SECRET_KEY = token_urlsafe(12)
ALGORITHM = "HS256"
EXPIRATION_TIME = timedelta(minutes=3)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_user(db: AsyncSession, login: str):
    result = await db.execute(
        select(models.User).filter(models.User.login == login))
    return result.scalars().first()


async def create_access_token(data: dict):
    token_encode = data.copy()
    expire = datetime.utcnow() + EXPIRATION_TIME

    token_encode.update({"exp": expire})
    return jwt.encode(token_encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: str = Depends(oauth2_scheme),
                           db: AsyncSession = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Something wrong with your credentials!!!",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        login: str = payload.get("sub")
        if login is None:
            raise credentials_exception
        token_data = TokenData(login=login)
    except JWTError:
        raise credentials_exception
    user = await get_user(db=db, login=token_data.login)
    if user is None:
        raise credentials_exception
    return user
