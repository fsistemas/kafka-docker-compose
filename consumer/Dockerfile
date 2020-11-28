FROM python:3.5

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./consumer.py app.py

ENV KAFKA_BOOTSTRAP_SERVERS 'kafka:9092'

ENTRYPOINT [ "python3", "/app/app.py" ]
