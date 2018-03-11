#!/usr/bin/env python

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='email-queue')

channel.basic_publish(exchange='', routing_key='email-queue', body='message')
print(' [x] Sent message')

connection.close()
