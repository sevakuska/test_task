FROM python:3.12-alpine
LABEL authors="sevakuska"

WORKDIR /test_task

COPY ./app /test_task/app
COPY ./core /test_task/core
COPY ./migrations /test_task/migrations
COPY ./alembic.ini /test_task/alembic.ini
COPY ./requirements.txt /test_task/requirements.txt

RUN pip install --no-cache-dir -U pip setuptools
RUN pip install --no-cache-dir -r /test_task/requirements.txt
RUN rm /test_task/requirements.txt
