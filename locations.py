import requests

#Fetching supermarket location ID, since some features on product API require it
def get_location_id(access_token):
    url="https://api.kroger.com/v1/locations?filter.limit=1"
    headers = {"Authorization": "Bearer " + access_token, "Cache-Control": "no-cache"}
    response = requests.get(url, headers=headers)
    if response.ok:
        return response.json()["data"][0]["locationId"]
    else:
        raise Exception("Location error: " + str(response.status_code) + ", " + response.text)