# pull official base image / вытаскиваем официальное базовое изображение
FROM python:3.9.6-alpine

# set work directory / устанавливаем рабочую директорию
# сюда пренесутся все файлы из BASE_DIR
WORKDIR /usr/src/ecodomskotom

# set environment variables / устанавливаем переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies / установка postgres
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies / устанаваливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy entrypoint.sh / копируем команду точки входа
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/ecodomskotom/entrypoint.sh
RUN chmod +x /usr/src/ecodomskotom/entrypoint.sh

# copy project / копируем проект
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/ecodomskotom/entrypoint.sh"]