import pika
import os
import time
import requests
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@rabbit-host/%2f')
params = pika.URLParameters(url)
params.socket_timeout = 5


connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    #time.sleep(body.count(b'.'))
    time.sleep(int(body))
    print(" [x] Done")
    url="http://10.203.63.229:15000/add?task="+str(int(body))
    r = requests.get(url)
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()
