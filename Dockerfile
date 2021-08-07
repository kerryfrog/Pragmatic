
FROM python:3.9.0

WORKDIR /home/

RUN echo "testing123"

RUN git clone https://github.com/kerryfrog/Pragmatic.git

WORKDIR /home/Pragmatic/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-_#$rw3%0hd-mqs^t()9in_%#h-x8vh&ed629h6uc&u%#m38het" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000" ]