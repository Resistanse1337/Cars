# Cars
В файле api_test.py примеры некоторых запросов

POST /auth/users/ - создание пользователя
POST /auth/token/login/ - авторизация
/cars/ - получение, добавление, обновление, удаление 
POST /cars/ - можно прикрепить в запросе .xlsx или .csv для загрузки в БД(по ключу upload_files)
/cars/?make_file=csv - получение .csv файла
/cars/?make_file=xlsx - получение .xlsx файла
