![workflow_status](https://github.com/bour89/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?event=push)

* * *
### Описание:
* * *

API для сервиса **Yamdb**.

Основные функции и особенности:

- Самостоятельная регистрация пользователей
- Аутентификация по JWT токену
- Просмотр и редактирование своего профиля после регистрации и аутентификации
- Просмотр информации о произведениях, их категориях и жанрах, отзывов и комментариев к ним \- доступен всем пользователям, включая анонимных
- Добавление отзывов и комментариев \- доступно аутентифицированным пользователям
- Модерирование отзывов и комментариев (модераторами и администраторами)
- Добавление произведений, их категорий и жанров \- доступно администраторам

## Запуск проекта
### 0. Клонировать репозиторий
### 1. Подготовить окружение
- Установить [Docker](https://docs.docker.com/get-docker/)
- Установите [docker-compose](https://docs.docker.com/compose/install/)
- Перейти в директорию проекта с docker-compose.yaml (по умолчанию: корень проекта)

### 2. Создать файл переменных среды
Создать в текущей папке файл .env со следующим содержимым:
```bash
SECRET_KEY=mysecretkey                  # секретный ключ Django (установите свой)
DB_ENGINE=django.db.backends.postgresql # работаем с БД PostgreSQL
DB_NAME=postgres                        # имя базы данных
POSTGRES_USER=postgres                  # имя пользователя БД
POSTGRES_PASSWORD=postgres              # пароль пользователя БД (установите свой)
DB_HOST=db                              # название сервиса (контейнера)
DB_PORT=5432                            # порт для подключения к БД
```

### 3. Собрать и запустить контейнеры Docker
```bash
docker-compose up --build -d
```

### 4. Выполнить миграцию базы данных
```bash
docker-compose exec web python manage.py migrate
```

### 5. Заполнить базу данных тестовыми данными

Копируем файл с базами данных в папку app

```
docker cp fixtures.json <id контенера>:/app
```

запускаем команду для загрузки баз
```
docker-compose exec web python manage.py loaddata fixtures.json
```

### 6. Собрать статические данные
```bash
docker-compose exec web python manage.py collectstatic
```

### 7. Проверить работоспособность проекта
- Корень проекта: http://localhost/api/v1/
- Админинстрирование: http://localhost/admin
- Документация: http://localhost/redoc


### Авторы
- [Артем Тимашков](https://github.com/Bour89):