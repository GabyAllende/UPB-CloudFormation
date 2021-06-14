
import json
import boto3
import os

users_table = os.environ['MOVIES_TABLE']

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(users_table)

def getMovie(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"] # "/user/123"
    array_path = path.split("/") # ["", "user", "123"]
    user_id = array_path[-1]
    
    # response = table.get_item(
    #     Key={
    #         'pk': user_id,
    #         'sk': 'age'
    #     }
    # )
    # item = response['Item']
    # print(item)
    return {
        'statusCode': 200,
        'body': json.dumps("success")
    }
    
def putMovie(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"] # "/user/123"
    array_path = path.split("/") # ["", "user", "123"]
    user_id = array_path[-1]
    
    body = event["body"] #"{\n\t\"name\": \"Jack\",\n\t\"last_name\": \"Click\",\n\t\"age\": 21\n}"
    body_object = json.loads(body)
    
    
    # table.put_item(
    #     Item={
    #         'pk': user_id,
    #         'sk': 'age',
    #         'name': body_object['name'],
    #         'last_name': body_object['last_name'],
    #         'age': body_object['age']
    #     }
    # )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

def roomsPerDay(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"] # "/user/123"
    array_path = path.split("/") # ["", "user", "123"]
    user_id = array_path[-1]
    
    # response = table.get_item(
    #     Key={
    #         'pk': user_id,
    #         'sk': 'age'
    #     }
    # )
    # item = response['Item']
    # print(item)
    return {
        'statusCode': 200,
        'body': json.dumps("success")
    }
    
    