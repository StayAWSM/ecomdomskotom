FROM python:3.10.9-slim

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev gettext cron openssh-client flake8 locales vim \
    tree nodejs npm

WORKDIR /ecodomskotom

COPY . .

RUN pip install -r requirements.txt
