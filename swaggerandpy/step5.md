# create a swagger file

goto editor.swagger.io and delete the contents,

*WIP* check for autogen tab?

take a couple of minutes to read over  
https://swagger.io/docs/specification/2-0/basic-structure/

now try and write your own, the RHS will let you know what to write

hints: 

I created a correct.yaml, it appears to work, but doesn't populate the swagger ui page right, are the consumers/producers in the right place? - remember you have validated it

ideas:  
- generate a flask file from editor and save it here and work from that


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