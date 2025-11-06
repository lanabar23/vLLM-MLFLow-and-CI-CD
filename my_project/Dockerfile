FROM python:3.10-slim-buster

WORKDIR /my_project

COPY . .

RUN pip install Flask

CMD ["python", "src/server/server.py"]