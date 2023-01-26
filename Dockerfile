# pull official base image / вытаскиваем официальное базовое изображение
FROM python:3.9.6-alpine

# set work directory / устанавливаем рабочую директорию
WORKDIR /usr/src/app

# set environment variables / устанавливаем переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies / устанаваливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project / копируем проект
COPY . .