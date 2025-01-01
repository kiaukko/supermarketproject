import requests
from requests.auth import HTTPBasicAuth

def get_access_token(client_id, client_secret):
    url = "https://api.kroger.com/v1/connect/oauth2/token"
    # Määritetään, että pyydetään nimenomaan pääsyä sovellukselle, ei käyttäjälle ja sallittaan scopeen tuotetietojen haku.
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
    # Tulostetaan vastaus
    if response.ok:
        return response.json().get("access_token")
    else:
        raise Exception("Authentication error: " + str(response.status_code) + ", " + response.text)