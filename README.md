# Запуск через консоль
## Установка виртуального окружения
`python -m venv venv`
## Зайти в виртуальное окружение
linux: `source venv/bin/activate`
win: `source venv/Scripts/activate`
## Установить зависимости
`pip install -r requirements.txt`
## Перейти в директорию
`cd weather_me`
## Заупстить проект
`python manage.py runserver 0.0.0.0:8000`

# Запуск через docker
## Забилдить образ
`sudo docker build -t weather_me:latest .`
## Запустить контейнер с пробросом портов
`docker run -d -p 8000:8000 weather_me:latest`

## Стек
Docker, Django
## Использовано
Только докер, остальное в превью
По запросу реализую все, используя React (MUI для автозаполнения), JWT Tokens и docker-compose
