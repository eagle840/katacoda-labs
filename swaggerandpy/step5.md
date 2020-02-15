# create a swagger file

goto editor.swagger.io and delete the contents,

now try and write your own, the RHS will let you know what to write

hints: 


*WIP*  soltuion:

swagger: "2.0"
info:
  title: "my first swagger doc"
  version: "1"
paths:
  "/people":
    get: 
      summary: "my first get statement"
      responses: 
        200:
          description: ok