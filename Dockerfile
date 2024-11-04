
FROM python:3.10


WORKDIR /app


COPY . /app


RUN pip install -r requirements.txt


CMD python manage.py migrate && python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:$PORT

