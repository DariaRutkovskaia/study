import datetime as dt

import requests

USERNAME = "dariarutkovskaia"
TOKEN = "qazxcdews"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

## Create user
# response = requests.post( url=pixela_endpoint, json=user_params)
# print(response.text)


## Create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_configuration = {
    "id": "graph1",
    "name": "python",
    "unit": "min",
    "type": "int",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_configuration, headers=headers)
# print(response.text)


##Create Pixel

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = dt.datetime.now()
formatted_date = today.strftime("%Y%m%d")
minutes = input("How many minutes have you studied today? ")

pixel_params = {
    "date": formatted_date,
    "quantity": minutes,
}
# p_response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(p_response.text)

## Update Pixel
# new_data = input("How many minutes? ")
# update_params = {
#     "quantity": new_data,
# }
# pixel_endpoint_update = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"
# update_response = requests.put(url=pixel_endpoint_update, json=update_params, headers=headers)
# print(update_response.text)


##Delete Pixel

# pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_date}"
# delete_response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(delete_response.text)