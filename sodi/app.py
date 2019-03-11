
from chalice import Chalice
import boto3
from boto3.dynamodb.conditions import Key, Attr

app = Chalice(app_name='sodi')

dynamodb = boto3.resource('dynamodb',region_name='eu-central-1')
table = dynamodb.Table('sodi')


@app.route('/')
def index():
    return {
        'Service': 'sody',
        'Description': 'Graffity and Streetart database API'
    }

@app.route('/location')
def get_location():
    try:
        response = table.scan(FilterExpression=Attr('location').eq('Santiago'))
        items = response['Items']

        return items
    except:
        return "Error"

@app.route('/item')
def get_item():
    response = table.get_item(
       Key={
            'sodiuid': '2019-03-11T13:51:26,65677',
            'screen_name': 'Gio_L9'
        }
    )

    item = response['Item']
    geo = item['geolocation']
    loc = item['location']

    return geo







