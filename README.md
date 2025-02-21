# PyPoster

Простая социальная сеть с лентой постов и авторизацией пользователей

## Основной стек:

- FastAPI
- SQLAlchemy
- Postgres + asyncpg

- Poetry
- black
- uvicorn


## Roadmap
- [x] Структура проекта
- [x] Подключение к базе данных
- [ ] Подключить pydantic-settings
- [ ] Летна постов



#### Запуск приложения
```bash
uvicorn src.main:app --port 8000 --reload
```

#### Документация:
http://127.0.0.1:8000/docs


## DEVELOP




## Полезные ссылки:
FastAPI Best Practices:
https://github.com/zhanymkanov/fastapi-best-practices

Database:
https://fastapi.tiangolo.com/tutorial/sql-databases/

Settings Management:
https://docs.pydantic.dev/latest/concepts/pydantic_settings/#usage