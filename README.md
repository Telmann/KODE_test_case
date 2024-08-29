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
    - 🔒[PyJWT](https://pyjwt.readthedocs.io/en/stable/) для получения JWT-токена для аутентификации.
    - [Я.Спеллер](https://yandex.ru/dev/speller/doc/ru/concepts/api-overview?ysclid=m0fdi2dd3r506654470) для валидации текста.
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

## При тестировании приложения с помощью SwaggerUI:
### Советую проводить авторизацию с помощью замочков перед попыткой обратиться к /notes 
![image](https://github.com/user-attachments/assets/ae041894-c470-4b70-ba8d-4b80dc3b5c97)
![image](https://github.com/user-attachments/assets/0251ce60-7c8e-46fa-bfed-2c7bc77322e4)

## Интерактивная документация по API
![image](https://github.com/user-attachments/assets/03fb8f69-1a5d-49c8-8532-51ad0749af0b)

## Кратко про существующие эндпоинты:
    - **POST /registration/**: Регистрация. Добавляет нового пользователя в базу данных. 
    - **POST /token**: Аутентифицирует пользователя и выдает токен доступа JWT. Проверяет указанные имя пользователя и пароль и, если они верны, генерирует JWT-токен доступа.
    - **POST /notes**: Создает новую заметку для текущего аутентифицированного пользователя. Проверяет содержимое на наличие ошибок с помощью [Яндекс.Спеллер](https://yandex.ru/dev/speller/doc/ru/concepts/api-overview?ysclid=m0fdi2dd3r506654470) и, если ошибок нет, сохраняет заметку в базе данных.
    - **GET /notes**: Получает из базы данных все заметки для текущего аутентифицированного пользователя.


## Интересная ошибка с которой я столкнулся
<details><summary>Подробнее</summary><br>
Использовал последнюю версию pytest(8.3.2) и получал [ошибку](https://github.com/pytest-dev/pytest-asyncio/issues/830) на самом первом тесте(при запуске тестов через Docker).
В результате пришлось использовать версию 8.2.1



