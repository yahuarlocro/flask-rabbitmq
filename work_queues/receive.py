import pika
import sys
import os


def main():
    connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()

    # make sure that the queue already exists
    channel.queue_declare(queue='hello')

    # meesages are received from the queue with a callback function, executed
    # by the pika library
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    # tell rabbitmq that this callback function receives messages from the
    # queue
    channel.basic_consume(queue='hello',
                          on_message_callback=callback, auto_ack=True)

    # never-ending loop that waits for data and runs callbacks whenever
    # necessary
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    # run programm and catch KeyboardInterrupt during program shutdown.
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
