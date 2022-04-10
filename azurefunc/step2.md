# more advanced

Taked from:  https://docs.microsoft.com/en-us/samples/azure-samples/functions-python-pytorch-tutorial/functions-python-pytorch-tutorial/

`cd ~`{{execute}}

`git clone https://github.com/Azure-Samples/functions-python-pytorch-tutorial.git`{{execute}}


# Activate virtualenv
`mkdir start`{{execute}}
`cd start`{{execute}}
`python -m venv .venv`{{execute}}
`source .venv/bin/activate`{{execute}}

# Initialize function app
`func init --worker-runtime python`{{execute}}
`func new --name classify --template "HTTP trigger"`{{execute}}
Copy resources into the classify folder, assuming you run these commands from start
`cp ../resources/predict.py classify`{{execute}}
`cp ../resources/labels.txt classify`{{execute}}

ADD the text in the github page to the requirements 

`pip install --no-cache-dir -r requirements.txt`{{execute}}

FOLLOW OTHER INSTRUCTIONS


# Run the local function
Run `func start`{{execute}} from within the start folder with the virtual environment activated.
Run http://localhost:7071/api/classify?img=https://raw.githubusercontent.com/gvashishtha/functions-pytorch/master/resources/assets/Bernese-Mountain-Dog-Temperament-long.jpg

# BUILD AND RUN


