#!/usr/bin/python

import time
from kafka import SimpleProducer, KafkaClient
from kafka.common import LeaderNotAvailableError

def print_response(i,response=None):
    if response:
        print(i , 'Error: {0}'.format(response[0].error)),
        print('Offset: {0}'.format(response[0].offset))


def main():
    kafka = KafkaClient("mykafkaslave.example.com:6667")

    producer = SimpleProducer(kafka)

    topic = b'testkafka'

    cnt = 0
    while(cnt < 10000):
            msg = b'Hello World - 1 - '
            cnt = cnt + 1

            msg += "%d" %(cnt)

            try:
                print_response(cnt,producer.send_messages(topic, msg))
            except LeaderNotAvailableError:
                print_response(cnt,producer.send_messages(topic, msg))

    kafka.close()

if __name__ == "__main__":
    main()

