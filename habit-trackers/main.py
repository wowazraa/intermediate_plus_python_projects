import requests
from datetime import *

USERNAME = "azradrinn"
TOKEN = "1A2z3r4a5"
GRAPH_ID = "graph1"
TODAY_DATE = datetime.now().strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": TODAY_DATE,
    "quantity": input("How many km did you cycle today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixel_creation_endpoint}/{TODAY_DATE}"

new_pixel_data = {
    "quantity": "16.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixel_creation_endpoint}/{TODAY_DATE}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

