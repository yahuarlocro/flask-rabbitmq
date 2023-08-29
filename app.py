from flask import Flask
import pika
from connection import RabbitMQConnection

app = Flask(__name__)


queue_name = 'my_task_queue'

@app.route('/')
def index():
    return 'welcome to NDVI orders'


@app.route('/order/<service>')
def send_order(service):
    # create connection and order queue
    with RabbitMQConnection(host='localhost', queue_name=queue_name) as rc:

        # publish message to exchange
        rc.basic_publish(exchange='', routing_key=queue_name, body=service, properties= pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))

    print(" [x] Sent %r" % service)
    return 'order was sent'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
