# KODE_test_case

## Стек
- ⚡ [**FastAPI**](https://fastapi.tiangolo.com) Для API/backend на Python.
    - 🧰 [SQLAlchemy](https://www.sqlalchemy.org/) Для взаимодействия с базой данных (ORM).
    - 🔍 [Pydantic](https://docs.pydantic.dev), используется FastAPI для валидации данных и управления настройками.
    - 💾 [PostgreSQL](https://www.postgresql.org) в качестве SQL БД.
    - :unicorn: [Uvicorn](https://www.uvicorn.org/), Веб-сервер ASGI для Python. (при запуске приложения/сервиса через docker используется gunicorn)
    - [pip](https://pip.pypa.io/en/stable/) в качестве стандартного пакетного менеджера. ![Зависимости зафиксированы](https://img.shields.io/badge/зависимости_зафиксированы-using%20pip%20freeze-blue)
    - [yapf](https://github.com/google/yapf) для автоматического форматирования кода в проекте.
    - [pytest](https://docs.pytest.org/en/stable/) + [pytest-asyncio](https://pypi.org/project/pytest-asyncio/) для тестирования приложения. Плагин pytest-asyncio обеспечивает поддержку coroutines в качестве тестовых функций. Позволяет использовать await внутри тестов.
    - 🐋[Docker](https://www.docker.com/) Запуск сервиса и требуемой им инфраструктуры проводится в docker контейнерах.
## Task / Задание
[Ссылка на задание](https://docs.yandex.ru/docs/view?url=ya-mail%3A%2F%2F187180859512588299%2F1.2&name=Python.%D0%A2%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D0%BE%D0%B5%20%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%202024.pdf&uid=1317911669) 
## Инструкция по запуску и тестированию сервиса с помощью 🐋Docker🐋
### 1.  Клонируйте репозиторий
    bash команда: git clone https://github.com/Telmann/KODE_test_case.git
### 2.  Откройте терминал (перейдите в директорию проекта)
    выполните: docker compose up --build test
    данная команда запустит тесты и после их успешного проведения вы увидите что-то похожее:
  ![image](https://github.com/user-attachments/assets/5317c19c-077f-4704-ad81-fe7ff2a06f94)
### 2.  Далее для запуска приложения
    выполните: docker compose up --build app
### 3. Готово! Приложение будет доступно по адресу: http://127.0.0.1:9999/docs#/
