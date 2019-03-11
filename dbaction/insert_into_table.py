import boto3
from _datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('sodi')

"""
table.put_item(
   Item={
        'username': 'ruanb',
        'first_name': 'ruan',
        'last_name': 'bekker',
        'age': 30,
        'account_type': 'administrator',
        'location': 'unknown'
    }
)


table.put_item(
   Item={
        'sodiuid':datetime.now().strftime('%Y%m%d_%H%M%S.%s'),
        'username': 'Gio_L9',
        'geolocation': {'lat': '-33.59353805', 'lon': '-70.5593418'},
        'user_name': 'giovanni letelier',
        'screen_name': 'Gio_L9',
        'location': 'Santiago',
        'text': '#arteurbano #urbanart  #saintseiya  #graffiti en Puente Alto, Chile https://t.co/PZlAYznMDO',
        'lang': 'uncknown',
        'text_en': 'not translated',
        'sentiment_pol': '0.0',
        'sentiment_sub': '0.0',
        'timestamp': '2019-03-11T13:51:26Z'
   }
)
"""

table.put_item(
   Item=

          {'sodiuid': '20190311_235118.1552341078', 'geolocation': {'lat': '40.670879549999995', 'lon': '-73.8311875'}, 'user_name': 'Bark&Bone Dog Walkers', 'screen_name': 'barknbonenyc', 'location': 'Astoria, NY', 'text': 'Luna has an eye for cheerful color 😉🐶🎨♥️ #toyaussie #streetart #dogsofinstagram #dog #dogs #nyc… https://t.co/46HrJes7eX ', 'lang': 'en ', 'timestamp': '2019-03-11T21:49:34Z'}


)

