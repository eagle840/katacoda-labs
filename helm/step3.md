# create your own

we'll install the sample chart provided by helm. 

`helm create examplechart`{{execute}}

`cd examplechart`{{execute}}

`tree`{{execute}}

take a read of the chart file

`cat Chart.yaml`{{execute}}

The charts folder is for dependant charts for this chart, but we won't using these in this demo.

The values yaml file is for values that you'll want to change every now and then. EG a service port number.

Now

`cd ..`{{execute}}

`helm install new-chart examplechart/ --values examplechart/values.yaml`{{execute}}

`helm list -A`{{execute}}

