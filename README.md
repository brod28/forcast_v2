Installation: Windows:

download and install python 3

open CMD:

cd {project folder}

pip install virtualenv

virtualenv env

env\scripts\activate

pip install -r requirements.txt

python manage.py runserver

Forcast is an API with 2 endpoints

method Post api/auth/login parameters: 1.username 2.password

response: token

method GET api/forcast/today/{city_name} for Authorization expecting http header 'Authorization' and value 'Token {token_from_login_api}'

example: curl -v -H @{'Authorization' = 'Token cbfc105679b3d1eede2d6d4e5bb3873178c6f9de'} http://127.0.0.1:8000/api/forcast/today/new%20york