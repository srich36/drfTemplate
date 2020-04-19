FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app/backend

WORKDIR /app/backend

ADD . /app/backend

RUN apt-get update && apt-get install -y libsasl2-dev python3-dev libldap2-dev libssl-dev libcairo2-dev pango1.0-tests && pip install -r requirements/base.txt