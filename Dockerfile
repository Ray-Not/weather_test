FROM python:3.8-slim

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

CMD ["python", "weather_me/manage.py", "runserver", "0.0.0.0:8000"]
