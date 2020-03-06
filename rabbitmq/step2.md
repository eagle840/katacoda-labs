# Hello World! using python

https://www.rabbitmq.com/tutorials/tutorial-one-python.html

`python -m pip install pika --upgrade`{{execute}}

https://pypi.org/project/pika/


we need the ip of the rabbit container

`RabbitIP = ${docker inspect some-rabbit | jq -r .[0].NetworkSettings.IPAddress}`{{execute}}

And replace 'localhost' in each python file

`sed s/localhost/${RabbitIP}/g send.py`{{execute}}
`sed s/localhost/${RabbitIP}/g receive.py`{{execute}}

`python receive.py`{{execute}}

`python send.py`{{execute}}

