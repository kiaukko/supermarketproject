CREATE DATABASE supermarket;

-- 1. Recipes Table
CREATE TABLE Recipes (
    recipe_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- 2. Ingredients Table
CREATE TABLE Ingredients (
    ingredient_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- 3. Recipe_Ingredients Table
CREATE TABLE Recipe_Ingredients (
    recipe_id INT NOT NULL,
    ingredient_id INT NOT NULL,
    PRIMARY KEY (recipe_id, ingredient_id),
    FOREIGN KEY (recipe_id) REFERENCES Recipes (recipe_id) ON DELETE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES Ingredients (ingredient_id) ON DELETE CASCADE
);

-- 4. Products Table
CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- 5. Ingredient_Products Table
CREATE TABLE Ingredient_Products (
    ingredient_id INT NOT NULL,
    product_id INT NOT NULL,
    PRIMARY KEY (ingredient_id, product_id),
    FOREIGN KEY (ingredient_id) REFERENCES Ingredients (ingredient_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES Products (product_id) ON DELETE CASCADE
);

-- 6. Carts Table
CREATE TABLE Carts (
    cart_id SERIAL PRIMARY KEY,
    recipe_id INT NOT NULL,
    FOREIGN KEY (recipe_id) REFERENCES Recipes (recipe_id) ON DELETE CASCADE
);

-- 7. Cart_Selections Table
CREATE TABLE Cart_Selections (
    cart_id INT NOT NULL,
    product_id INT NOT NULL,
    PRIMARY KEY (cart_id, product_id),
    FOREIGN KEY (cart_id) REFERENCES Carts (cart_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES Products (product_id) ON DELETE CASCADE
);