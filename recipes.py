import requests

def fetch_random_recipe():
    url="https://www.themealdb.com/api/json/v1/1/random.php"
    response = requests.get(url)
    if response.ok:
        meal = response.json()['meals'][0] #Save the meal into a variable so we can access the ingredients below it
        # Use a set to prevent duplicates
        ingredients = set()

        # Add each ingredient to the set one by one
        for key, value in meal.items():
            if key.startswith("strIngredient") and value:  # Check that the value is not empty
                ingredients.add(value)
        return ingredients
    else:
        raise print("Recipe error: " + str(response.status_code) + ", " + response.text)