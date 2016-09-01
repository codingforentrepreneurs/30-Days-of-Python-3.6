import json
import requests

from requests_oauthlib import OAuth1


consumer_key= 'NZTJrWhij8kemtAXmfyhyA'
consumer_secret = 'JtcAesDkKuNltcKdwR7NEaUkgm8'
token = 'TCipoxU_lYo55-F3rS10XdnN6f-3-KQI'
token_secret = '5gAZ99Arn2x_LIOVM25AWy8H84c'



url ='https://api.yelp.com/v2/search?term=food&location=San+Francisco'
r = requests.get(url, auth=auth)

def do_search(term='Food', location='San Francisco'):
    base_url = 'https://api.yelp.com/v2/search'
    term = term.replace(' ', '+')
    location = location.replace(' ', '+')
    url = "{base_url}?term={term}&location={location}".format(base_url=base_url, 
                        term=term, 
                        location=location)
    auth = OAuth1(consumer_key, 
            consumer_secret, 
            token, 
            token_secret)
    r = requests.get(url, auth=auth)
    return r.json(), r.text



json_data, text_data = do_search()
python_data = json.loads(text_data)
print(json.dumps(json_data, indent=4, sort_keys=True))


for i in json_data['businesses']:
    print(i["name"])
    print(i["phone"])
    print(i["location"]["display_address"])
    print(i["location"]["city"])




