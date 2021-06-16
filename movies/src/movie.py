
import json
import boto3
import os
from boto3.dynamodb.conditions import Key, Attr


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
    
    res = table.put_item(
        Item={
            'pk': movie_id,
            'sk': 'mov_info',
            'main_actors': body_object['main_actors'],
            'title': body_object['title'],
            'year': body_object['year']
        })
     
    return {
        'statusCode': 200,
        'body': json.dumps("Agregado correctamente")
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
    
def getAvailableRooms(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"] # "/user/123"
    array_path = path.split("/") # ["", "user", "123"]
    movie_id = array_path[-1]
    print("Llega hasta aca")
    
    table2 = table.scan(FilterExpression=Attr('pk').eq(movie_id) & Attr('sk').begins_with("room_"))
    data = table2['Items']
    print("data")
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
        'body': json.dumps(data)
    }
    
def getAudience(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"] # "/user/123"
    array_path = path.split("/") # ["", "user", "123"]/ "/rooms/{room_id}/movies/{movie_id}"
    movie_id = array_path[-1]
    room_id = array_path[-3]
    print("Llega hasta aca")
    
    q1 = table.scan(FilterExpression=Attr('pk').eq(movie_id) & Attr('sk').eq(room_id))
    q2 = table.scan(FilterExpression=Attr('pk').eq(room_id) & Attr('sk').begins_with("person_"))
    data1 = q1['Items']
    data2 = q2['Items']
    
    temp = []
    
    for x in data1:
        for y in data2:
            if x['schedule'] == y['schedule']:
                temp.append(y)
    
    
    print(temp)
    
    
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
        'body': json.dumps(data1)
    }
    
    
def getAvailableRooms2(event, context):
    print(json.dumps({"running": True}))
    print(json.dumps(event))
    
    path = event["path"] # "/user/123"
    array_path = path.split("/") # ["", "user", "123"]
    movie_id = array_path[-1]
    print("Llega hasta aca")
    
    table2 = table.scan(FilterExpression=Attr('pk').eq(movie_id) & Attr('sk').begins_with("room_"))
    data = table2['Items']
    print("data")
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
        'body': json.dumps(data)
    }
    