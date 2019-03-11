import boto3

dynamodb = boto3.resource('dynamodb',region_name='eu-central-1' )

table = dynamodb.create_table(
    TableName='sodi',
    KeySchema= [
        {
            'AttributeName': 'sodiuid',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'screen_name',
            'KeyType': 'RANGE'
        }
    ],

    AttributeDefinitions=[

        {
            'AttributeName': 'sodiuid',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'screen_name',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)

table.meta.client.get_waiter('table_exists').wait(TableName='sodi')
print(table.item_count)