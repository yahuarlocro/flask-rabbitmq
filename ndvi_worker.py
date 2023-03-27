import time
import sys
import os
from connection import RabbitMQConnection
from app import queue_name

def main():

    # Receiving messages from the queue is more complex. It works by
    # subscribing a callback function to a queue. Whenever we receive a
    # message, this callback function is called by the Pika library. In our
    # case this function will print on the screen the contents of the message.
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())


        # simulate a job that takes long. every point is one second
        time.sleep(body.count(b'.'))

        print(" [x] Done")

        # Message aknowledgement:
        # send a proper acknowledgment from the worker, once we're done with a 
        # task
        ch.basic_ack(delivery_tag = method.delivery_tag)

    # make sure that the queue exists. We do this beacuse we do not know in
    # which order were the applications executed. Creating a queue using
    # queue_declare is idempotent
    # queue_name = 'order'
    # queue_name = 'task_queue'

    with RabbitMQConnection(host='localhost', queue_name=queue_name) as rc:

        # fair dispatch
        # don't dispatch a new message to a worker until it has processed and 
        # acknowledged the previous one. Instead, it will dispatch it to the
        # next worker that is not still busy.
        rc.basic_qos(prefetch_count=1)

        #  tell RabbitMQ that this particular callback function should receive
        # messages from our order queue
        # when auto_ack is set to true, then no message aknowledgement will be 
        # sent in case a worker dies
        rc.basic_consume(queue=queue_name,
                         on_message_callback=callback)
                         #auto_ack=True)
        
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