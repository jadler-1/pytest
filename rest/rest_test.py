print('rest_test')

import requests
response = requests.get("http://api.open-notify.org/astros.json")
print(response)