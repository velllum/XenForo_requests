import codecs
import json

import requests

# url = 'https://infobit.space/api/threads/' # получили даные из новые темы
# url = 'https://infobit.space/api/posts/9839' # получили стаью по его ид ключь last_post_id
# url = 'https://infobit.space/api/nodes/' # получили подкатегории из главной категории "КАТАЛОГ ИНФОПРОДУКТОВ"
from config import key

url = 'https://infobit.space/api/nodes/11' # получили подкатегорию с данными из нее

headers = {'XF-Api-Key': key}

payload = {
    # "page": 20
}

r = requests.get(
    url=url,
    headers=headers,
    params=payload
)

r_json_ = json.dumps(r.json(), sort_keys=True, indent=4)
json_ = codecs.decode(r_json_, 'unicode_escape')
print(json_)
print(r.request.body)
