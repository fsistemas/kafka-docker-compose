#!/usr/bin/python3

from kafka import KafkaConsumer
import logging as log
import os
import random
import sys
import time

print("Start...")

# log.basicConfig(format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
#                 datefmt='%Y-%m-%d %H:%M:%S',
#                 level=log.INFO)

def main(args):
    bootsrap_server = os.environ['KAFKA_BOOTSTRAP_SERVERS']

    print("KAFKA_BOOTSTRAP_SERVERS: ", bootsrap_server )

    topic = "topic1"

    while True:
        try:
            # consume messages using KafkaConsumer
            consumer = KafkaConsumer(bootstrap_servers=bootsrap_server, auto_offset_reset='latest', enable_auto_commit=True, group_id="python")
            consumer.subscribe(topic)
            for msg in consumer:
                log.info("Consumer Record: \n{}".format(msg))
                print("Message: ", msg)
        except Exception as ex:
            log.error(str(ex))
            print(ex)

    print("DONE")

if __name__ == "__main__":
    main(sys.argv)
