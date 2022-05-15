FROM python:3

RUN apt update -y && apt install -y python3-pip python-dev

WORKDIR /app

RUN pip install Flask

COPY . .

EXPOSE 5000

CMD ["python", "./app.py"]