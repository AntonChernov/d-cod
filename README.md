# d-cod
h1 Создать virtualenv
=====================
virtualenv -p python3 venvname
***
Установить requirements
pip install -r requirements.txt

***

h1 Создать и настроить DB Postgres
=====================
***
установка -- sudo apt-get install postgresql postgresql-contrib
***
настройка DB
sudo -u postgres psql
***
Создание пользователя для базы
create user test2 with password 'test';
***
Создание DB
create database dcodetest;
***
Дать созданному пользователю права
grant all privileges on database dcodetest to test2;
***
Выйти из консоли Postgres
\q

h1 Запуск проэкта
=====================
***
Перейти в деррикторию /d_code/test_d_code/
прописать в консоли (виртуальное окружение должно быть активированно (комада --> source bin/activate команда зависит от
места запуска если запускать из корня проэкта то команда будет такой source ../bin/activate))  python parser.py
парсер загрузит данные в DB.
***
запустить тестовый сервер Django находясь в папке с файлом manage.py командой  python manage.py runserver
***
Перейти в браузере по ссылке: http://127.0.0.1:8000/main/
