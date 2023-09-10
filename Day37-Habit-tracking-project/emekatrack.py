from datetime import datetime
import requests


USERNAME = "victor-chiemeka"
TOKEN = "Vicemekusi123!@"
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
        "type": "int",
        "color": "shibafu"
        }

response = requests.post(url=graph_endpoint, json=config_graph)
print(response.text)


