import requests
from requests.auth import HTTPBasicAuth

def get_access_token(client_id, client_secret):
    url = "https://api.kroger.com/v1/connect/oauth2/token"
    
    #Specifying that access is requested for the application and fetching product information is in the scope.
    data = {
        "grant_type": "client_credentials",
        "scope": "product.compact"
    }
    response = requests.post(
        url,
        auth=HTTPBasicAuth(client_id, client_secret),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=data,
    )

    #Printing result
    if response.ok:
        return response.json().get("access_token")
    else:
        raise Exception("Authentication error: " + str(response.status_code) + ", " + response.text)