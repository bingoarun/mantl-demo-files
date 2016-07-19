#!/usr/bin/env python
import pika
import sys
import os
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@10.203.63.229/%2f')
params = pika.URLParameters(url)
params.socket_timeout = 5

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

#message = ' '.join(sys.argv[1:]) or "Hello World!"
messages = [
	'1',
	'5',
	'3',
 	'8',
	'6',
	'2',
        '7',
        '6',
        '5',
        '3' 
	]
for message in messages:
  channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
print(" [x] Sent all messages")
connection.close()
