import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('sodi')

response = table.scan(
    FilterExpression=Attr('location').eq('Santiago')
)

items = response['Items']
print(items)