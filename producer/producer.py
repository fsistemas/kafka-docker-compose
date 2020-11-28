#!/usr/bin/python3

from kafka import KafkaProducer
import logging as log
import os
import random
import sys
import time

log.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                level=log.INFO)

def send_message(bootsrap_server, topic, message):
    try:
        # produce message using KafkaProducer
        producer = KafkaProducer(bootstrap_servers=bootsrap_server)
        message_bytes = bytes(message, encoding='utf-8')
        producer.send(topic, value=message_bytes)
        producer.flush()
        log.info("Message published successfully: " + message)
        print("Message published successfully: ", message)
    except Exception as ex:
        log.error(str(ex))
        print(ex)

def main(args):
    bootsrap_server = os.environ['KAFKA_BOOTSTRAP_SERVERS']

    print("KAFKA_BOOTSTRAP_SERVERS: ", bootsrap_server )

    topic = "topic1"

    while True:
        message = "Hello from Kafka Python client. Random value: " + str(random.random())
        send_message(bootsrap_server, topic, message)
        time.sleep(5)

    print("DONE")

if __name__ == "__main__":
    main(sys.argv)
