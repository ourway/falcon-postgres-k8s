FROM python:latest AS BASE

WORKDIR /app
ARG FAL_VER
ENV FAL_VER=$FAL_VER


COPY app/requirements.txt requirements.txt
COPY app/app.py app.py

RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["gunicorn", "app", "-b", "0.0.0.0:80"]
