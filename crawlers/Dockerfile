FROM python:3.7

RUN mkdir /app
ADD /app /app
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:80 wsgi


