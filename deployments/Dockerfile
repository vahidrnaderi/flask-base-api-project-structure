# pull official base image
FROM python:3.12-slim

LABEL maintainer="Vahidreza Naderi <vahidrnaderi@gmail.com>"

EXPOSE 8080

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY ./run.sh .
COPY . .

# install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"]
