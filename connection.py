import pika


# class RabbitMQConnection(object):
#     # class RabbitMQConnection:
#     # def __init__(self, host, user, password, queue_name, port=5627):
#     def __init__(self, host, queue_name):
#         self.host = host
#         # self.user = user
#         # self.password = password
#         # self.port = port
#         self.queue_name = queue_name
#
#     def __enter__(self):
#
#         # credentials = pika.PlainCredentials(self.user, self.password)
#         parameters = pika.ConnectionParameters(
#             host=self.host,
#             # port=self.port,
#             # credentials=credentials
#         )
#         # connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
#         self.connection = pika.BlockingConnection(parameters)
#         self.channel = self.connection.channel()
#         self.channel.queue_declare(queue=self.queue_name)
#         return self.channel
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         self.connection.close()

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
# def __repr__(self):
#     return f"userID {self.user_id}"
