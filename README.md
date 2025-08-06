## Требования

- Docker и Docker Compose
- Python 3.10+
- uv

---

## Установка и запуск

1. Клонируйте репозиторий

   ```bash
   git clone git@github.com:malabr1sta/SQLAlchemy_practice.git
   cd SQLAlchemy_practice


2. Соберите и запустите контейнеры с помощью Docker Compose

   ```bash
   docker-compose up --build


3. Переименуйте файл окружения и загрузите переменные окружения из файла

   ```bash
   mv env_example .env
   source .env


3. Переименуйте файл окружения и загрузите переменные окружения из файла

   ```bash
   mv env_example .env
   source .env


4. Для запуска используйте

   ```bash
   uv run main.py


5. Для доступа к базе из контейнера используйте команду

   ```bash
   docker exec -it psql_server psql -U $DATABASE_USER -d $DATABASE_NAME
