import requests
import random

# Fetching products based on ingredient
def fetch_products(ingredient, location_id, access_token):
    url="https://api.kroger.com/v1/products?filter.term=" + ingredient + "&filter.limit=5&filter.locationId=" + location_id
    headers={"Authorization": "Bearer " + access_token, "Cache-Control": "no-cache"}
    response=requests.get(url, headers=headers)
    if response.ok:
        products = response.json().get("data", []) #Returning empty list if "data" doesnt exist
        if products:
            return {
                "ingredient": ingredient,
                "all_products": products, #simulating a situation where user is offered 5 products
                "selected_product": random.choice(products) #simulating the choice user makes
            }
    return {"ingredient": ingredient, "all_products": [], "selected_product": None} #if there are no products