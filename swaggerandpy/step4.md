
cp sim to v2

nano 

FIRST add  a simple GET to return a simplee text line

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