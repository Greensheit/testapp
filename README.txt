1. Необходимо в коммандной строке перейти в дирректорию с данным веб сервисом
2. Отредактировать файл docker-compose, изменив необходимые конфигурации(базы данных, хоста, порта)
3. Отредактировать файл Work/settings.py, изменив необходимые переменные (ALLOWED_HOSTS, DATABASES)
4. Выполнить миграции командами docker-compose run web python manage.py makemigrations и docker-compose run web python manage.py migrate
5. Выполнить комманду docker-compose up
6. POST запрос выполняется по адресу .../set/
7. GET запрос выполняется по адресу .../get/
