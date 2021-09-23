FROM python:3.9.0

WORKDIR /home/

RUN echo 'asdasqw'

RUN git clone https://github.com/soohyoen/djangoProject.git

WORKDIR /home/djangoProject/

RUN echo "SECRET_KEY=django-insecure-c!5obm$)lkt$y18+z#)d^27e$jeb+t4tx*0+606_n^_f1=^=1r" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash","-c", "python manage.py collectstatic --noinput --settings=djangoProject.settings.deploy && python manage.py migrate --settings=djangoProject.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=djangoProject.settings.deploy djangoProject.wsgi --bind 0.0.0.0:8000"]