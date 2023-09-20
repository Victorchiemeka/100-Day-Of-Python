import requests

url = "https://api.agify.io?name=michael"
response = requests.get(url)
# print(response.text)

data = response.json()
print(data)
