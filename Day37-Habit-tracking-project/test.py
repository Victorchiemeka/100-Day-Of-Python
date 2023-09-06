from datetime import datetime
import requests


USERNAME = "victor-emeka"
TOKEN = "Vicemeka127!@"
GRAPH_ID = "mygraph1"
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
        "id": GRAPH_ID,
        "name": "Coding graph",
        "unit": "hour",
        "type": "float",
        "color": "shibafu"
        }

header =  {
        "X-USER-TOKEN": TOKEN
        }

#response = requests.put(url=graph_endpoint, json=config_graph, headers=header)
#print(response.text)

pixel_creation =  f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

pixel_data = {
        "date": today.strftime("%Y%m%d"),
        "quantity":"4.5",

        }

response = requests.post(url=pixel_creation, json=pixel_data, headers=header)
print(response.text)
