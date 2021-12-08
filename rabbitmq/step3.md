# check the queues

`docker exec some-rabbit rabbitmqctl list_queues`{{execute}}


# work queues

https://www.rabbitmq.com/tutorials/tutorial-two-python.html

# open 2 terminals and run in each


`cat work.py`{{execute}}

we need to replace localhost with an ip

`RabbitIP=$(docker inspect some-rabbit | jq -r .[0].NetworkSettings.IPAddress)`{{execute}}

`echo $RabbitIP`{{execute}}

`sed -i "s/localhost/$RabbitIP/g" worker.py`{{execute}}

and run the worker

`python3 worker.py`{{execute}}

# in another

each . represents a second

`python3 new_task.py First message.`{{execute}}

`python3 new_task.py Second message..`{{execute}}

`python3 new_task.py Third message...`{{execute}}

`python3 new_task.py Fourth message....`{{execute}}

`python3 new_task.py Fifth message.....`{{execute}}

