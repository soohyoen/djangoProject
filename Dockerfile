FROM python:3.9.0

WORKDIR /home/

RUN echo 'dslkfmin'

RUN git clone https://github.com/soohyoen/djangoProject.git

WORKDIR /home/djangoProject/

RUN echo "SECRET_KEY=django-insecure-c!5obm$)lkt$y18+z#)d^27e$jeb+t4tx*0+606_n^_f1=^=1r" > .env

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]