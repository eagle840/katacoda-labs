# Run the simple python program.

This particular python program has had flasgger called, which allows you to take a swagger config file and incorperate into the program.

`ls`{{execute}}

lets take a look at the python program first.   Take note of the 'swagger_config.yml' file.

`cat simple_sum_swagger_api.py`{{execute}}

and take a look at the swagger file:

`cat swagger_config.yml`{{execute}}

WIP: The schema of the swagger file appears incorrect
WIP: ---------------------
Infact lets take a look at that file in the online swagger editor <https://editor.swagger.io/>

click on file and import url, and enter:

`https://raw.githubusercontent.com/bhattbhavesh91/swagger-python-flask-app/master/swagger_with_flask/swagger_config.yml`{{copy}}

Opps!  Looks like we need to add a version to this yaml file.

Add: `swagger: "2.0"`   to the top of the file

WIP: ----------------

# execute the program

we could run the python program as `python <programName.py>` however flask will default to the localhost access only, and on katacoda we need to access it from out side.

`export FLASK_APP=simple_sum_swagger_api.py; flask run --host 0.0.0.0 --port 8500`{{execute}}

when ready you can **ctrl-c** to exit the running program

lets open another terminal and check we are serving out this program to all incoming requests:

`netstat -tap`{{execute}}

(t: tcp, a: all, P: include the porcesss listing)

you should a python process running on 'local address' 0.0.0.0 and port 8500

https://[[HOST_SUBDOMAIN]]-8500-[[KATACODA_HOST]].environments.katacoda.com/

WIP: the last time I ran this it worked, now it's not. (was on 5000)

you can also see swagger serving up it's page at:

https://[[HOST_SUBDOMAIN]]-8500-[[KATACODA_HOST]].environments.katacoda.com/swagger

https://[[HOST_SUBDOMAIN]]-8500-[[KATACODA_HOST]].environments.katacoda.com/swagger/#!/default/post_add_2_numbers

In the right hand side you'll see an example, click on it and it'll populate the 'body' on the left and then click 'try it out' at the bottom of the page.