FROM python:3.6-alpine3.12
WORKDIR /app

COPY . /app
COPY requirements.txt .

RUN pip install unittest

CMD ["python","app.py"]