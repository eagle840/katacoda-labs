# more advanced

Taked from:  https://docs.microsoft.com/en-us/samples/azure-samples/functions-python-pytorch-tutorial/functions-python-pytorch-tutorial/

https://docs.microsoft.com/en-us/azure/azure-functions/machine-learning-pytorch?tabs=bash

`cd ~`{{execute}}

`git clone https://github.com/Azure-Samples/functions-python-pytorch-tutorial.git`{{execute}}

`cd functions-python-pytorch-tutorial`{{execute}}




# Initialize function app
`func init --worker-runtime python`{{execute}}
`func new --name classify --template "HTTP trigger"`

`func new --name classify"`{{execute}}

THE FOLLOWING IS MISSING THE SECOND ARD - are these cmds needed?

Copy resources into the classify folder, assuming you run these commands from start
`cp ./resources/predict.py classify/`{{execute}}
`cp ./resources/labels.txt classify/`{{execute}}


copy the following into __init__.py

```
import logging
import json
import azure.functions as func

from .predict import predict_image_from_url

def main(req: func.HttpRequest) -> func.HttpResponse:
    image_url = req.params.get('img')
    logging.info('Image URL received: ' + image_url)

    results = predict_image_from_url(image_url)

    headers = {
        "Content-type": "application/json",
        "Access-Control-Allow-Origin": "*"
    }

    return func.HttpResponse(json.dumps(results), headers = headers)

```
# dump the following
ADD the text in the github page to the requirements 

`pip install --no-cache-dir -r requirements.txt`{{execute}}

!the pip install is failing,
try this:


pip install -f https://download.pytorch.org/whl/torch_stable.html torch==1.5.0+cpu torchvision==0.6.0+cpu

FOLLOW OTHER INSTRUCTIONS
# dump the above 


# Run the local function
Run `func start`{{execute}} from within the start folder with the virtual environment activated.

we're going to classify the following picture: https://raw.githubusercontent.com/gvashishtha/functions-pytorch/master/resources/assets/Bernese-Mountain-Dog-Temperament-long.jpg

Run http://localhost:7071/api/classify?img=https://raw.githubusercontent.com/gvashishtha/functions-pytorch/master/resources/assets/Bernese-Mountain-Dog-Temperament-long.jpg

not sure the above will work, try    
- `curl -v http://localhost:7071/api/classify?img=https://raw.githubusercontent.com/gvashishtha/functions-pytorch/master/resources/assets/Bernese-Mountain-Dog-Temperament-long.jpg`{{execute}}
- https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com/api/HttpExample?name=Functions
- https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com/api/HttpExample?name=Functions/api/classify?img=https://raw.githubusercontent.com/gvashishtha/functions-pytorch/master/resources/assets/Bernese-Mountain-Dog-Temperament-long.jpg


Not getting the response I want

`curl -v http://localhost:7071/api/classify?img=https://raw.githubusercontent.com/gvashishtha/functions-pytorch/master/resources/assets/Bernese-Mountain-Dog-Temperament-long.jpg`{{execute "T2"}}


# BUILD AND RUN


`docker build . --tag azurefunc`{{execute}}

`docker run -p 8080:80 azurefunc`{{execute}}


