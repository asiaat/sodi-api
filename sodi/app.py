
from chalice import Chalice
import boto3
from boto3.dynamodb.conditions import Key, Attr
import json

app = Chalice(app_name='sodi')

dynamodb = boto3.resource('dynamodb',region_name='eu-central-1')
table = dynamodb.Table('sodi')


@app.route('/')
def index():
    return {
        'Service': 'sody',
        'Description': 'Graffity and Streetart database API'
    }

@app.route('/location/{place}')
def get_by_location(place):
    try:
        response = table.scan(FilterExpression=Attr('location').eq(place))
        items = response['Items']

        return json.dumps(items, indent=4, sort_keys=True)
    except:
        return "Error"

@app.route('/user/{screen_name}')
def get_by_user(screen_name):
    try:
        response = table.scan(FilterExpression=Attr('screen_name').eq(screen_name))
        items = response['Items']

        return json.dumps(items, indent=4, sort_keys=True)
    except:
        return "Error"

@app.route('/lang/{lang}')
def get_by_lang(lang):
    try:
        response = table.scan(FilterExpression=Attr('lang').eq(lang.strip()))
        items = response['Items']

        return json.dumps(items, indent=4, sort_keys=True)
    except:
        return "Error"

@app.route('/country/{country}')
def get_by_country(country):
    try:
        response = table.scan(FilterExpression=Attr('country').eq(country))
        items = response['Items']

        return json.dumps(items, indent=4, sort_keys=True)
    except:
        return "Error"







