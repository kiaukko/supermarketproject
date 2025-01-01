from concurrent.futures import ThreadPoolExecutor
from dotenv import load_dotenv
import os
from locations import get_location_id
from recipes import fetch_random_recipe
from products import fetch_products
from auth_handler import get_access_token

def main():
    # Configurations
    load_dotenv()
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    #Authentication
    access_token = get_access_token(client_id, client_secret)
    print("Access token acquired.")

    #Location ID
    location_id = get_location_id(access_token)
    print("Location ID: " + location_id)

    #Receipt and ingredients
    ingredients = fetch_random_recipe()
    print("Ingredients: " + ", ".join(ingredients))

    #Products
    #Use ThreadPoolExecutor to fetch products concurrently
    ingredient_products = {}

    with ThreadPoolExecutor(max_workers=min(10, len(ingredients))) as executor:
        futures = {executor.submit(fetch_products, ingredient, location_id, access_token): ingredient for ingredient in ingredients}
        for future in futures:
            result = future.result()
            if result["all_products"]:
                ingredient_products[result["ingredient"]] = result

    # Display results
    print("\nSummary of Selected Products:")
    for ingredient, products_info in ingredient_products.items():
        print("Ingredient: " + ingredient)
        print("All Products:")
        for product in products_info["all_products"]:
            print("  - Product ID: " + product["productId"])
        print("Selected Product: " + products_info["selected_product"]["productId"] + "\n")

if __name__ == "__main__":
    main()