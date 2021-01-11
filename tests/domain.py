import urllib.request
import json


with urllib.request.urlopen('http://crm.bpagency.ro/crm_data/data_base.json') as url:
    data = json.loads(url.read().decode())
    print(data)


# 'http://crm.bpagency.ro/crm_data/data_base.json'