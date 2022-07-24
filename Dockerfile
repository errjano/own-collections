FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN export PATH="$PATH:~/.yarn/bin"


RUN mkdir /code
RUN mkdir /code/logs
WORKDIR /code

ADD ./conf/requirements.txt /code/
RUN apk add --update \
    gcc \
    py-pip \
    build-base \
    git \
    wget \
    libxslt-dev \
    xmlsec-dev \
    mariadb-dev \
    libressl-dev

RUN pip install -r requirements.txt
ADD ./src/ /code/

ARG DJANGO_APP
ENV DJANGO_APP=${DJANGO_APP}
EXPOSE 8000

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:8000 ${DJANGO_APP}.wsgi:application"]
