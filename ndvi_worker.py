import sys
import os
from connection import RabbitMQConnection




def main():

    # Receiving messages from the queue is more complex. It works by
    # subscribing a callback function to a queue. Whenever we receive a 
    # message, this callback function is called by the Pika library. In our 
    # case this function will print on the screen the contents of the message.
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    
    
    # make sure that the queue exists. We do this beacuse we do not know in 
    # which order were the applications executed. Creating a queue using 
    # queue_declare is idempotent 
    queue_name = 'order'


    with RabbitMQConnection(host='localhost',queue_name=queue_name) as rc:

        #  tell RabbitMQ that this particular callback function should receive 
        # messages from our order queue
        rc.basic_consume(queue=queue_name,on_message_callback=callback, auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')

        # enter a never-ending loop that waits for data and runs callbacks
        #  whenever necessary
        rc.start_consuming()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

