
import json
import boto3
import os

movies_table = os.environ['MOVIES_TABLE']

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(movies_table)

def getMovie(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"] # "/user/123"
    array_path = path.split("/") # ["", "user", "123"]
    movie_id = array_path[-1]
    print("temp")
    response = table.get_item(
        Key={
            'pk': movie_id,
            'sk': 'mov_info'
        }
    )
    item = response['Item']
    print(item)
    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }
    
def putMovie(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"] # "/user/123"
    array_path = path.split("/") # ["", "user", "123"]
    movie_id = array_path[-1]
    
    body = event["body"] #"{\n\t\"name\": \"Jack\",\n\t\"last_name\": \"Click\",\n\t\"age\": 21\n}"
    body_object = json.loads(body)
    
    print(body_object['main_actors'])
    print(body_object['title'])
    print(body_object['year'])
    
    table.put_item(
        Item={
            'pk': movie_id,
            'sk': 'mov_info',
            'main_actors': body_object['main_actors'],
            'title': body_object['title'],
            'year': body_object['year']
        })
    # Item={
    #         'pk': movie_id,
    #         'sk': 'mov_info',
    #         'main_actors': 'Keira Knightley',
    #         'title': 'Orgullo y Prejuicio',
    #         'year': '2012'
    #     }
    table.put_item(Item)
    
    #item = item['Item']
    return {
        'statusCode': 200,
        'body': json.dumps("All good")
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
    
    