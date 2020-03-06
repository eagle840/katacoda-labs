# Hello World! using python

https://www.rabbitmq.com/tutorials/tutorial-one-python.html

`python -m pip install pika --upgrade`{{execute}}

https://pypi.org/project/pika/


we need the ip of the rabbit container

`RabbitIP=$(docker inspect some-rabbit | jq -r .[0].NetworkSettings.IPAddress)`{{execute}}

`echo $RabbitIP`{{execute}}

And replace 'localhost' in each python file

`sed -i "s/localhost/$RabbitIP/g" send.py`{{execute}}

`sed -i "s/localhost/$RabbitIP/g" receive.py`{{execute}}

Now send a message to RabbitMQ:

`python send.py`{{execute}}

If you jump over to the management page, you'll see the msg in the queue in the Overview and the Queues tab.

Let's receive that msg,

`python receive.py`{{execute}}



 Lets another terminal and exe send 3 times:

`python send.py`{{execute T2}}

In the orginal terminal you'll see them coming back, and the msg rate's in the mgmnt console changing.

Ctrl-C to exit the program

