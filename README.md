# flask-rabbitmq

http://localhost:15672
user: guest
password: guest


# DEFINITIONS

## Producer
A program that sends messages

## Queue
It is the post box. Messages can only be stored in a queue. It is bound by
the host's memory and disks limits. It is just a large message buffer

## Consumer
A program that wait to receive messages



# HELLO WORLD

RabittMQ is a message broker system. RabbitMq is a post box, a post office,
and a letter carrier

A message must always be sent by a ***exchange***. Cannot be sent direct
to a queue


# WORK QUEUES

A work queue is used to distribute time-consuming tasks among workers

The idea of work queues is to avoid waiting for a task to complete. Instead
tasks is scheduled to be completed later

We encapsulate the task as a message and send it to the queue. A worker
running on the background (or more) will execute the job

This concept is especially useful in web applications where it's impossible
to handle a complex task during a short HTTP request window.

## Message Acknowlegment

What happens if a workers dies or is stopped ? Messages dispatched and
processed by this worker are lost

If a worker dies, we want the message to be delivered to another worker.

In order to be sure that messages are not lost, RabbitMQ supports ***message 
Acknowlegment***. An ack(nowledgement) is sent back by the consumer to tell
RabbitMQ that a particular message had been received, processed and that
RabbitMQ is free to delete it.

If a worker dies (its channel is closed, connection is closed, or TCP
connection is lost) without sending an acknowledgment, RabbitMQ understands
that message was not processed and it is delivered to another worker (consumer)

A timeout (30 minutes by default) is enforced on consumer delivery
acknowledgement. This helps detect buggy (stuck) consumers that never 
acknowledge deliveries. You can increase this timeout

Manual message acknowledgments are turned on by default. In previous examples
we explicitly turned them off via the ***auto_ack=True*** flag. It's time to
remove this flag and send a proper acknowledgment from the worker, once we're
done with a task.

Acknowlegments should be sent to the same channel, otherwise will result in a 
channel-level protocol exception
