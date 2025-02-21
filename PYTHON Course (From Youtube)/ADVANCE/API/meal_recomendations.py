import requests
import json
import sqlite3

conn = sqlite3.connect("MealTracker.db")
cursor = conn.cursor()


cursor.execute('''
        CREATE TABLE IF NOT EXISTS meals_table (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                ingredients TEXT NOT NULL
                )
''')

def api_handling():
    url = "https://api.freeapi.app/api/v1/public/meals?page=1&limit=50&query=all"
    response = requests.get(url)
    super_data = response.json()
    if super_data["success"]:
        data = super_data["data"]
        meal_data = data["data"]
        return meal_data
    else:
        raise Exception("❌ Error fetching meal data!")

def list_all_meal(meals):
    meal_count = 0
    for index,meal in enumerate(meals,start=1):
        meal_name = meal.get("strMeal")
        category = meal.get("strCategory")
        ingredients = ingredients_fatcher(meals,index)
        print("*" * 30)
        print(f"  index: {index}")
        print(f"🍲Meal name: {meal_name}")
        print(f"🧐Category: {category}")
        print(f"🍴ingredients: {ingredients}")
        print("*" * 30)
        meal_count += 1
    return meal_count,meals

def ingredients_fatcher(meals,index):
    ingredient_list = []
    for i in range(1,21):
        ingredient = meals[index-1]["strIngredient" + str(i)]
        if ingredient != "":
            ingredient_list.append((ingredient).lower())
    ingredient_json = json.dumps(ingredient_list)
    return ingredient_json


def save_meal(meals,meal_count):
    choice = int(input("Enter Your meal index: "))
    if 1<= choice <= meal_count:
        name = meals[choice-1]["strMeal"]
        category = meals[choice-1]["strCategory"]
        ingredients = ingredients_fatcher(meals,choice)
        cursor.execute("INSERT INTO meals_table (name,category,ingredients) VALUES (?,?,?)", (name,category,ingredients))
    conn.commit()

def display_saved():
    cursor.execute("SELECT COUNT(*) FROM meals_table")
    count = cursor.fetchone()[0]
    if count == 0:
        print("-->No Meal saved please save Meal first!")
        return
    cursor.execute("SELECT * FROM meals_table")
    for meals in cursor.fetchall():
        print("*" * 30)
        print(f"  index: {meals[0]}")
        print(f"🍲Meal name: {meals[1]}")
        print(f"🧐Category: {meals[2]}")
        print(f"🍴Ingredients: {meals[3]}")
    print("=" * 50)

    delete_choice = input("Do you want to delete any meal(Y/N)?: ")
    if delete_choice == "Y" or delete_choice == "y":
        delete_saved_meal()
    print("=" * 50)

def delete_saved_meal():
    index = int(input("Enter index number to delete meal: "))
    cursor.execute("DElETE FROM meals_table WHERE id = ?", (index,))
    conn.commit()

def filter(meals):
    user_category = input("Enter preferred category (e.g., Vegetarian, Chicken, Side): ").lower()
    user_ingredient = input("Enter a preferred ingredient (e.g., Chicken, Cheese, Rice): ").lower()
    user_cuisine = input("Enter preferred cuisine (e.g., Italian, Indian, Chinese): ").lower()
    
    filter_meal = []
    meal_count = 0
    for index,meal in enumerate(meals,start=1):
        category = (meal.get("strCategory")).lower()
        ingredients = ingredients_fatcher(meals,index)
        # print(ingredients)
        cuisine = (meal.get("strArea")).lower()

        if category not in user_category:
            continue
        if user_ingredient not in ingredients:
            continue
        if user_cuisine not in cuisine:
            continue
        
        filter_meal.append(meal)
        meal_count +=1
    return filter_meal,meal_count



def main():
    meals = api_handling()
    while True:
        print("=" * 50)
        print("1. List all meals")
        print("2. display saved")
        print("3. Recomend meal by your preference")
        print("4. Exit")
        choice = input("Enter Your choice: ")
        print("=" * 50)

        match choice:
            case "1":
                meal_count,listed_meals = list_all_meal(meals)
                want_to_save = input("Do You want to save this meal(Y/N)?:")
                if 1 <= meal_count and (want_to_save == "Y" or want_to_save == "y"):
                    save_meal(listed_meals,meal_count)
            case "2":
                display_saved() 
            case "3":
                filtered_meal,meal_count = filter(meals)
                # print(filtered_meal)
                if filtered_meal:
                    for index,meal in enumerate(filtered_meal,start=1):
                        print("*" * 30)
                        print(f"index: {index} \nmeal name: {meal["strMeal"]} \nCategory: {meal["strCategory"]} \ncuisine: {meal["strArea"]}")
                        print("*" * 30)
                    save_choice = input("Do you want to save Your meal(Y/N)?: ")
                    if save_choice == "Y" or save_choice == "y":
                        save_meal(filtered_meal,meal_count)
                else:
                    print("meal not matched!")
            case "4":
                break
            case __:
                print("Invalid Choice!")
    conn.close()

if __name__ == "__main__":
    main()