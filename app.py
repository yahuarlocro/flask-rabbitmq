from flask import Flask
from connection import RabbitMQConnection

app = Flask(__name__)


@app.route('/')
def index():
    return 'welcome to NDVI orders'


@app.route('/order/<service>')
def send_order(service):
    queue_name = 'order'

    # create connection and order queue
    with RabbitMQConnection(host='localhost',queue_name=queue_name) as rc:
        
        # publish message to exchange
        rc.basic_publish(exchange='',routing_key=queue_name, body=service)



    print(" [x] Sent 'order was sent'")
    return 'order was sent'



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
