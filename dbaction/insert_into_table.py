import boto3

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
"""

table.put_item(
   Item={
        'sodiuid':'2019-03-11T13:51:26,65677',
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
