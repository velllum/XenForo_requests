import codecs
import json

import requests

url = 'https://infobit.space/api/threads/'

headers = {'XF-Api-Key': 'sQc4HYWadjy7Q5-O8wM0ImSxlAWyEQyR'}

payload = {
    # 'api_bypass_permissions': 1,
    # 'key': 1
}

r = requests.get(
    url=url,
    headers=headers,
    params=payload
)

r_json_ = json.dumps(r.json(), sort_keys=True, indent=4)
json_ = codecs.decode(r_json_, 'unicode_escape')
print(json_)
