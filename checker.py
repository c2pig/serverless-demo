import requests
import json

# API key to use google custom search
googleApiKey = 'AIzaSyDeMhboTQQwXJ-XkJ8AcCiQ7NB4TARFsf4'

# CX value, which custom site to search for - price.com.hk as example
priceDotCom = '000314962227041223191:b0d-3yx8meq'

def lambda_handler(event, context):
   print event;
   requestURL = 'https://www.googleapis.com/customsearch/v1?key={apikey}&cx={site}&q={query}'.format(apikey = googleApiKey, site = priceDotCom, query= event['queryStringParameters']['query'])
   r = requests.get(requestURL)
   data = json.loads(r.text)
   # printResult(data)
   response = {
     "statusCode": 200,
     "body": json.dumps(data['items'])
   }
   return response;
