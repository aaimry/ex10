Склонируйте проект и создайте виртуальное окружение
```
python3 -m venv venv
```

Активируйте виртуальное окружение командой
```
source . venv/bin/activate
```

Установите зависимости командой
```
pip install -r requrements.txt
```

Cоздайте в директории source  файл .env и заполните его по образцу
```
SECRET_KEY= SECRET_KEY
DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_NAME=db_name
DB_USER=db_user
DB_PASSWORD=db_password
DB_HOST=host
DB_PORT=port
DEBUG=on

```

Примените миграции командой
```
./manage.py migrate
```

Загрузите фиксиуры командой
```
./manage.py loaddata fixtures/auth.json
.manage.py loaddata fixtures/dump.json
```