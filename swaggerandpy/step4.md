
cp sim to v2

nano 

FIRST add  a simple GET to return a simplee text line, insert the following under the index section:

```
@app.route("/hello")
def  hello():
     return "hello world!"
```{{copy}}

https://[[HOST_SUBDOMAIN]]-8500-[[KATACODA_HOST]].environments.katacoda.com/hello

should return hello world

add '@swag_from("swagger_config.yml")'
and you can now open swagger and see it in there

https://[[HOST_SUBDOMAIN]]-8500-[[KATACODA_HOST]].environments.katacoda.com/swagger

*WIP* why?

## lets make it interactive

In the follow is a piece of code that will take a number as an input with the url /12/return.
However it will generate an erro, see if you can fix the code to return the number.

```
@app.route("/<int:id>/return")
def  returnnum(id):
     return "returned number!"
```{{copy}}

*WIP* do a solution for below: (note have to return a string and add try and except)

```
@app.route("/<int:id>/return")
def  returnnum(id):
     numstring = str(id)
     return numstring
```

```
def multiple_2_numbers(num1, num2):
    output = {"multiply_2_numbers": 0}
    x2_numbers = num1 * num2
    output["multiply_2_numbers"] = x2_numbers
    return output
```{{copy}}


```
@app.route("/multiple_2_numbers", methods=["POST"])
@swag_from("swagger_config.yml")
def add_numbers():
    input_json = request.get_json()
    try:
        num1 = int(input_json["x1"])
        num2 = int(input_json["x2"])
        res = multiple_2_numbers(num1, num2)
    except:
        res = {"success": False, "message": "Unknown error"}

    return json.dumps(res)
```{{copy}}