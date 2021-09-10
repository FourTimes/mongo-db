```py

import requests
from requests.auth import HTTPDigestAuth
import json

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

data = {
    'databaseName': 'admin',
    'password': 'dodonotdo123',
    'roles': [
        {
            'databaseName': 'my_database',
            'roleName': 'dbAdmin'
        }
    ],
    'username': 'demo'
    }

# variable section
GroupId = "xxxxxxxxxxxxx"

PublicKey = "xxxxxxxxxx"

PrivateKey = "xxxxxxxx-2691-xxxxx-bf97-xxxxxxxxx"

url = "https://cloud.mongodb.com/api/atlas/v1.0/groups/" + GroupId + "/databaseUsers/admin/demo"

_result = requests.patch(url, auth=HTTPDigestAuth(
    PublicKey, PrivateKey), headers=headers, data=json.dumps(data))
print(_result.json())


```
