FROM python:3.9.10-slim-buster

ADD ./ /usr/src/app

WORKDIR /usr/src/app
ENV FLASK_APP=app

#COPY /app/requirements.txt ./
RUN apt update \
  && apt install -y gcc
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "uwsgi", "--ini", "/usr/src/app/uwsgi.ini" ]