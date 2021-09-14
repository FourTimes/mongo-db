import boto3
import json
import string
import random
import requests
from requests.auth import HTTPDigestAuth
import os

# VARIABLE SECTION

REGION=os.environ['REGION']



# Random password generators
def generate_random_password():
    characters = list(string.ascii_letters + string.digits + "!#$%^&*()")
    length = 16
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))
    random.shuffle(password)
    return ("".join(password))

# aws login session init


def init_aws_session():
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=REGION
    )
    return client

# aws get session


def get_secret(key):
    client = init_aws_session()
    get_secret_value_response = client.get_secret_value(SecretId=key)[
        'SecretString']
    return json.loads(get_secret_value_response)

# aws update secret key


def update_secret(key, secret=generate_random_password()):
    print(secret)
    client = init_aws_session()
    client.update_secret(SecretId=key, SecretString=json.dumps({key: secret}))
    return get_secret(key)

# update the mongodb password via rest api.


"""
Create the secrets in aws secret manager => the name of mongodb-dev

{
  "GroupId": "xxxxxxxx",
  "PublicKey": "aaaaaaa",
  "PrivateKey": "aaaaa-bbbbb-ccccc-ddddd-eeeee",
  "username": "demo",
  "database": "my_database"
}

"""


def update_db_user_password(api_key, mongoAuth, password=generate_random_password()):
    mongoCredentials = get_secret(mongoAuth)
    for key, value in mongoCredentials.items():
        if key == 'GroupId':
            GroupId = value
        if key == 'PublicKey':
            PublicKey = value
        if key == 'PrivateKey':
            PrivateKey = value
        if key == 'username':
            username = value
        if key == 'database':
            database = value

    # update the password in aws secret manager
    update_secret(api_key, password)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    url = "https://cloud.mongodb.com/api/atlas/v1.0/groups/" + \
        GroupId + "/databaseUsers/admin/" + username

    data = {
        'databaseName': 'admin',
        'username': username,
        'password': password,
        'roles': [
            {
                'databaseName': database,
                'roleName': 'dbAdmin'
            }
        ]
    }

    # Update the password via Mongo REST API.
    dbUserPasswordUpdate = requests.patch(url, auth=HTTPDigestAuth(
        PublicKey, PrivateKey), headers=headers, data=json.dumps(data))
    return dbUserPasswordUpdate.json()


def lambda_handler(event, context):
    print(update_db_user_password('api_key', 'mongodb-dev'))

