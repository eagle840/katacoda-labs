# Delete the stack

Lets check the status of the stack

`pulumi stack`

note the Owner (your user name),   
Also note on line 7 the 'pulumi:pulumi:Stack" value. It's your <project>-<dev stack>  values

Lets delete the stack, type in, replacing the username, project and devstack.

`pumumi destory -s <userName>/<project>/<Dev stack>`

If you haven't already, be sure to look around your pulumi project in the website.