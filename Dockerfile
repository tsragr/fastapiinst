FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /usr/src/FastApiCRUD

COPY ./requirements.txt /usr/src/FastApiCRUD/requirements.txt
RUN pip install -r /usr/src/FastApiCRUD/requirements.txt

COPY . .

EXPOSE 8000