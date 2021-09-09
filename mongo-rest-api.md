```sh
# database users lists
curl --user "xxxxx:xx-xx-xxxx-xxxx-xxxxxx" --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request GET "https://cloud.mongodb.com/api/atlas/v1.0/groups/xxxxxxxx/databaseUsers?pretty=true"

```

```bash
# user creation
curl --user "xxxxx:xx-xx-xxxx-xxxx-xxxxxx"  --digest \
     --header "Accept: application/json" \
     --header "Content-Type: application/json" \
     --include \
     --request POST "https://cloud.mongodb.com/api/atlas/v1.0/groups/xxxxxxxx/databaseUsers" \
     --data '
       {
         "databaseName": "admin",
         "password": "changeme123",
         "roles": [{
           "databaseName": "my_database",
           "roleName": "readWrite"
         }],
         "username": "david"
       }'

```
