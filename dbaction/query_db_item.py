import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('sodi')

response = table.get_item(
   Key={
        'sodiuid': '2019-03-11T13:51:26,65677',
        'screen_name': 'Gio_L9'
    }
)

item = response['Item']
geo = item['geolocation']
loc = item['location']

print(item)
print("Location: " + loc)