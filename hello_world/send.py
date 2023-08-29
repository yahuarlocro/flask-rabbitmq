import pika

# SENDING
# stablich connection with rabbitmq server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# create a quere were the message will be delivered
channel.queue_declare(queue='hello')

# declare exchange to specify exactly to which queue the message should go
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')

# debug
print(" [x] Sent 'Hello World!'")

# flush network buffers and confirm message was delivered
connection.close()
#
