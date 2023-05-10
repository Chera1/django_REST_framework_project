# Запуск проекта django_REST_framework_project
Предварительно нужно скачать poetry и установить зависимости:
  
```
    python -m pip install --upgrade pip
    pip install poetry==1.4.2
    poetry --version
    poetry install
```

Выполняем команду `poetry run python manage.py makemigrations` для создания миграций на основе наших моделей
После применяем наши миграции командой `poetry run python manage.py migrate`

## Пример запросов к API
### Получение списка данных:
- GET /api/actors/
- GET /api/films/
### Получение токенов jwt:
POST /api/token/ с ключами username и password
### Получение доступа для изменения данных:
GET /api/film/<int:pk> c авторизацией через токен, выданный выше.
### Создание фильмов для авторизованных пользователей: 
POST /api/films/
### Удаление фильма (только для персонала(is_staff)):
DELETE /api/filmdelete/<int:pk>
### Для обновления фильма авторизованными пользователями:
PUT /api/film/<int:pk>
