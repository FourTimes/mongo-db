# mongo-db

 import the MongoDB public GPG Key

    wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -

Install gnupg and its required libraries using the following command

    sudo apt-get install gnupg

Once installed, retry importing the key

    wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -


Create a list file for MongoDB

    vim /etc/apt/sources.list.d/mongodb-org-5.0.list

    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list

Reload local package database

    sudo apt-get update

Install the MongoDB packages

    sudo apt-get install -y mongodb-org

NOTE:

    Although you can specify any available version of MongoDB, apt-get will upgrade the packages when a newer version becomes available. To prevent unintended upgrades, you can pin the package at the currently installed version

Command

    echo "mongodb-org hold" | sudo dpkg --set-selections
    echo "mongodb-org-database hold" | sudo dpkg --set-selections
    echo "mongodb-org-server hold" | sudo dpkg --set-selections
    echo "mongodb-org-shell hold" | sudo dpkg --set-selections
    echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
    echo "mongodb-org-tools hold" | sudo dpkg --set-selections

Start the MongoDB

    sudo systemctl start mongod

Enable the MongoDB 

    sudo systemctl enable mongod

Restart the MongoDB

    sudo systemctl restart mongod

Begin using MongoDB (verify with MongoDB shell)

    $ mongo 

Enable remote access in MongoDB

    sudo vim /etc/mongod.conf

    bindIp: 0.0.0.0

Restart the MongoDB

    sudo systemctl restart mongod

Verify the remote access use nc Command

    nc -zv mongodb_server_ip 27017

Enable user access in MongoDB

    $ mongo
    > show dbs
    > use admin
    > db.createUser({ user: "username",pwd: passwordPrompt(),roles: [{role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]})
    > exit

Enabling Authentication

    sudo vim /etc/mongod.conf'

        # Scroll down to find the commented-out security section:
        # Then add the authorization parameter and set it to enabled. When you’re done, the lines should look like this:

        security:
          authorization: enabled

Restart the MongoDB

    sudo systemctl restart mongod

Check the MongoDB

    sudo systemctl status mongod

Verification

    $ mongo -u username -p --authenticationDatabase admin
    > show dbs