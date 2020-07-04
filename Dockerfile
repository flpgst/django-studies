FROM python:3

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN useradd -ms /bin/bash django

RUN pip install Django

USER django

ENV PYTHONUNBUFFERED 1

ENV PATH $PATH:/home/django/.local/bin

WORKDIR /home/django/app

ADD . .

CMD python manage.py runserver 0:8000

EXPOSE 8000