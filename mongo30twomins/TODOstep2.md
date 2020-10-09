# add code to query with node.js

!add ports 27017 on the compose file - done!

steps:

create:
    npm init -y
    npm install mongodb

create app.js

const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');

// const url = 'mongodb://localhost:27017';
const dbName = 'circulation';
const user = encodeURIComponent('root');
const password = encodeURIComponent('admin');
const authMechanism = 'DEFAULT';

// Connection URL
const url = `mongodb://${user}:${password}@localhost:27017/?authMechanism=${authMechanism}`;

async function main(){
    const client = new MongoClient(url);
    await client.connect();

    const admin = client.db(dbName).admin();
    console.log(await admin.serverStatus());
    console.log(await admin.listDatabases());
    client.close();
}

main();


....................................

!note: still getting an authN failed
see:
http://mongodb.github.io/node-mongodb-native/3.6/tutorials/connect/authenticating/



