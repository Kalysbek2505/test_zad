
FROM python:3.10


WORKDIR /app


COPY . /app


RUN pip install -r requirements.txt


CMD python manage.py collectstatic --noinput && \
    python manage.py migrate && \
    gunicorn config.wsgi:application --bind 0.0.0.0:$PORT