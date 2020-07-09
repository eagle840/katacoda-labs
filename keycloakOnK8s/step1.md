# Setup keycloak

WORK IN PROGRESS

Let's do some updates



---- following not needed
 `apt update -y`{{execute}}
 `apt install openjdk-8-jre-headless -y`{{execute}}
----

Let's start by downloading the Keycloak distribution:

`curl https://downloads.jboss.org/keycloak/7.0.0/keycloak-7.0.0.zip --output keycloak-7.0.0.zip`{{execute}}

and unzip it:

`unzip keycloak-7.0.0.zip`{{execute}}

`cd keycloak-7.0.0/bin`{{execute}}

And run this script to add a admin user:

`JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre/`{{execute}}

`./add-user-keycloak.sh -r master -u admin -p admin`{{execute}}

WIP if this cmd fails restart scenario


and start the server (about 2mins)
`./standalone.sh -b 0.0.0.0`{{execute}}


Login to the Keycloak Admin Console at:

WIP: some deployments fail, restart the lab if problems logging into the admin console.

https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com/auth/admin


On the landing page, click on Administration Console. This will bring you to a login form. Enter the following credentials: admin / admin.

# Create a realm

You are now on the Master realm configuration page, but let's create our own realm.   

At the top of the left menu, hover over Master. When a button to add a Realm appears, click it. Give the realm a name, such as katacoda, and click create.  


# Creating a realm role

Now we need to create a realm role.

On the left menu, click on Roles. You see a list of roles. On the upper right of the table, look for Add Role and click that button.

Give the role a name, such as user, and save it. 


# Creating an user   

The last step to complete the configuration of the realm is to create a user.

On the left menu, click Users. You see a list of users. On the right of the table, look for Add user. Click that button.

Only the username is mandatory, so let's fill in that field with 'test' and click save.

You are now on the details page of the new user. We still need to perform two tasks:

Give the user credentials.   
Assign the role user to our test user.   
Create Initial Credentials   
Click on the Credentials tab and add a new password: test. Confirm the password. Notice the Temporary checkbox. If it is enabled, the user has to change this password at the first login. You can decide if you want to change that setting or leave it unchanged for this lesson. Click Reset Password.   

# Assign the Realm Role to the User   

The last step is to assign the role user to our test user. Click on the tab Role Mappings. In Available Roles, you see the user role.

# Create an OAuth client

On the lhs, click on clients, and then create

lets call it 'kube-cluster'

WIP need the openID Connect discovery std end point keyclockserver.com:socket443/auth/realms/<realmName>   
find them here: on  left hand side,   Configure>Realm Settings>General>Endpoints>'clock on OpenID...'

