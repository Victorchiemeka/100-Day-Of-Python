import requests


USERNAME = "victor-emeka"
TOKEN = "Vicemeka127!@"

pixela_endpoint = "https://pixe.la/v1/users"
user_param = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
        }
#response = requests.post(url=pixela_endpoint, json=user_param)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

config_graph = {
        "id": "mygraph1",
        "name": "Coding graph",
        "unit": "km",
        "type": "float",
        "color": "shibafu"
        }

header =  {
        "X-USER-TOKEN": TOKEN
        }
response = requests.post(url=graph_endpoint, json=config_graph, headers=header)
print(response.text)
