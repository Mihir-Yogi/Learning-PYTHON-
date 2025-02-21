import requests
import json 
import sqlite3

conn = sqlite3.connect("rendom_product.db")
cursor = conn.cursor()

cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price TEXT NOT NULL,
            category TEXT NOT NULL
            )
        ''')

def api_hendling():
    url = "https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches"
    response = requests.get(url)
    response_data = response.json()
    super_data = response_data["data"]
    data = super_data["data"]
    return data

def list_all_product(product_data):
    for index,data in enumerate(product_data,start=1):
        name = data.get("title")
        price = data.get("price")
        category = data.get("category")
        print("*" * 30)
        print(f"Index: {index}")
        print(f"Name: {name}")
        print(f"Category: {category}")
        print(f"Price: ₹{price}")
        print("*" * 30)

def add_to_cart(product_data):
    list_all_product(product_data)
    index_no = int(input("Enter your index number to add to cart: "))
    name = product_data[index_no-1]["title"]
    category = product_data[index_no-1]["category"]
    price = product_data[index_no-1]["price"]
    cursor.execute("INSERT INTO products (name,price,category) VALUES (?,?,?)", (name,category,price))
    conn.commit()

def display_cart():
    cursor.execute("SELECT * FROM products")
    for data in cursor.fetchall():
        print("*" * 30)
        print(f"Index: {data[0]}")
        print(f"Name: {data[1]}")
        print(f"Category: {data[2]}")
        print(f"Price: {data[3]}")
        print("*" * 30) 

def remove_from_cart():
    display_cart()
    delete_index = int(input("Enter Index number to delete cart item: "))
    cursor.execute("DELETE FROM products WHERE id = ?",(delete_index,))
    conn.commit()

def main():
    product_data = api_hendling()
    while True:
        print("=" * 50)
        print("Random Product")
        print("1. List all Products")
        print("2. add to cart")
        print("3. display cart")
        print("4. remove from Cart")
        print("5. Exit")
        choice = input("Enter Your choice: ")
        print("=" * 50)

        match choice:
            case "1":
                list_all_product(product_data)
            case "2":
                add_to_cart(product_data)
            case "3":
                display_cart()
            case "4":
                remove_from_cart()
            case "5":
                break
            case __:
                print("Invalid Choice")
    conn.close()


if __name__ == "__main__":
    main()