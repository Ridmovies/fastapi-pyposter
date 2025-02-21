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
- [x] Подключить pydantic-settings
- [x] Подключить Alembic alembic init --template async alembic
- [ ] Летна постов
    - [x] Модель поста
    - [ ] Создание поста



#### Запуск приложения
```bash
uvicorn src.main:app --port 8000 --reload
```

#### Документация:
http://127.0.0.1:8000/docs


## DEVELOP
## Alembic
Изменить настройки env.py
```
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)
target_metadata = Base.metadata
```


### Creating async an Environment
```bash
alembic init --template async alembic
```

### Generate first migration
```bash
alembic revision --autogenerate -m "initial migration"
```

### Apply generated migration to the database:
```bash
alembic upgrade head
```

### Rolls back the last applied migration.
```bash
alembic downgrade -1
```




## Полезные ссылки:
FastAPI Best Practices:
https://github.com/zhanymkanov/fastapi-best-practices

Database:
https://fastapi.tiangolo.com/tutorial/sql-databases/

Settings Management:
https://docs.pydantic.dev/latest/concepts/pydantic_settings/#usage