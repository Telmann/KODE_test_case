import asyncio
import random
import string
from typing import AsyncGenerator

import pytest
from httpx import AsyncClient

from app.main import app

letters = string.ascii_letters

login: str = ''.join(random.choice(letters) for i in range(5))
password: str = ''.join(random.choice(letters) for k in range(6))

url: str = "http://127.0.0.1:8000/"


@pytest.fixture(scope="session")
def event_loop() -> AsyncGenerator:
    loop: asyncio.AbstractEventLoop = asyncio.new_event_loop()
    yield loop
    loop.close()


# Тестируем регистрацию и добавление юзера в БД
@pytest.mark.asyncio
async def test_registration() -> None:
    async with AsyncClient(app=app, base_url=url) as ac:
        response = await ac.post("/registration",
                                 json={
                                     "login": login,
                                     "password": password
                                 })
    assert response.status_code == 200
    assert response.json()["message"] == "New user added to the db!"


# Тестируем аутентификацию и получение токена + post-запрос к '/notes'
@pytest.mark.asyncio
async def test_post_note() -> None:
    async with AsyncClient(app=app, base_url=url) as ac:
        response = await ac.post("/token",
                                 data={
                                     "username": login,
                                     "password": password
                                 })
        token: str = response.json()["access_token"]
    assert response.status_code == 200

    async with AsyncClient(app=app, base_url=url) as ac:
        content: str = "Новый тест создан!"
        response2 = await ac.post("/notes",
                                  params={"content": content},
                                  headers={"Authorization": f"Bearer {token}"})
    assert response2.status_code == 200
    assert response2.json()['content'] == content


# Тестируем аутентификацию и получение токена + get-запрос к '/notes'
@pytest.mark.asyncio
async def test_get_notes() -> None:
    async with AsyncClient(app=app, base_url=url) as ac:
        response = await ac.post("/token",
                                 data={
                                     "username": login,
                                     "password": password
                                 })
        token: str = response.json()["access_token"]
    assert response.status_code == 200

    async with AsyncClient(app=app, base_url=url) as ac:
        response2 = await ac.get("/notes",
                                 headers={"Authorization": f"Bearer {token}"})
    assert response2.status_code == 200


# Тестируем exception при неверном логине|пароле
@pytest.mark.asyncio
async def test_wrong_login_pass() -> None:
    async with AsyncClient(app=app, base_url=url) as ac:
        response = await ac.post("/token",
                                 data={
                                     "username": 'wrong_username',
                                     "password": 'wrong_password'
                                 })
    assert response.status_code == 401
    assert response.json()["detail"] == "Wrong username or password!!!"


# Тестируем exception при неверном токене
@pytest.mark.asyncio
async def test_wrong_token() -> None:
    wrong_token: str = "wrong token"
    async with AsyncClient(app=app, base_url=url) as ac:
        response = await ac.post(
            "/notes", headers={"Authorization": f"Bearer {wrong_token}"})
    assert response.status_code == 401
    assert response.json(
    )["detail"] == "Something wrong with your credentials!!!"


# Тестируем exception при попытке запостить заметку с орфографическими ошибками
@pytest.mark.asyncio
async def test_invalid_text() -> None:
    async with AsyncClient(app=app, base_url=url) as ac:
        response = await ac.post("/token",
                                 data={
                                     "username": login,
                                     "password": password
                                 })
        token: str = response.json()["access_token"]
    assert response.status_code == 200

    wrong_content: str = 'сабака!'
    async with AsyncClient(app=app, base_url=url) as ac:
        response2 = await ac.post("/notes",
                                  params={"content": wrong_content},
                                  headers={"Authorization": f"Bearer {token}"})
    assert response2.status_code == 400
    assert response2.json(
    )["detail"]["message"] == "В вашем тексте обнаружены ошибки!"
