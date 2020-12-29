FROM python:latest AS deployment

WORKDIR /app
ARG FAL_VER
ENV FAL_VER=$FAL_VER


COPY app/. .

RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["gunicorn", "app", "-b", "0.0.0.0:80", "-w", "4"]



FROM python:latest AS local

WORKDIR /app/dev

RUN apt-get update -y
RUN apt-get install vim -y

COPY app/requirements.txt .
RUN pip install -r requirements.txt
RUN pip install pgcli ipython

RUN echo '\n\
set nocompatible\n\
syntax on' \
>> /root/.vimrc

EXPOSE 80

ENTRYPOINT ["gunicorn", "app", "-b", "0.0.0.0:80", "--reload"]
