from pymongo import MongoClient
from bson import ObjectId
import requests
import json

client = MongoClient("mongodb+srv://mihiryogi:mihiryogi123@shopingcart1.ltkku.mongodb.net/")

db = client["ShopingCartManager"]
cartCollection = db["cart"]

def api_handling():
    url = "https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=all"
    response = requests.get(url)
    json_response = response.json()
    super_data = json_response["data"]
    product_data = super_data["data"]
    return product_data

def list_all_products(product_data):
    for index,product in enumerate(product_data,start=1):
        title = product["title"]
        category = product["category"]
        price = product["price"]
        print("*" * 30)
        print(f"index: {index}")
        print(f"Title: {title}")
        print(f"categoy: {category}")
        print(f"price: ${price}")
        print("*" * 30)

def save_cart(product_data):
    list_all_products(product_data)
    print("=" * 50)
    user_index = int(input("Enter product index for add to cart: "))

    for index,product in enumerate(product_data,start=1):
        if user_index == index:
            title = product["title"]
            category = product["category"]
            price = product["price"]
            cartCollection.insert_one({"title": title, "category": category, "price": price})
            print("product added in Cart.")
    print("=" * 50)

def show_cart():
    for product in cartCollection.find():
        print("*" * 30)
        print(f"id: {product.get("_id")}")
        print(f"Title: {product.get("title")}")
        print(f"Category: {product.get("category")}")
        print(f"Price: {product.get("price")}")
        print("*" * 30)

def delete_from_cart():
    show_cart()
    print("=" * 50)
    userEntered_id = ObjectId(input("Enter Product id to Delete form cart: "))
    cartCollection.delete_one({"_id": userEntered_id})
    print("=" * 50)

def main():
    product_data = api_handling()
    while True:
        print("=" * 50)
        print("--Shoping Cart Manager--")
        print("1. List all Products")
        print("2. Save to cart")
        print("3. Show Cart")
        print("4. Delete from cart")
        print("5. Exit")
        choice = input("Enter Your Choice: ")
        print("=" * 50)

        match choice:
            case "1":
                list_all_products(product_data)
            case "2":
                save_cart(product_data)
            case "3":
                show_cart()
            case "4":
                delete_from_cart()
            case "5":
                break
            case __:
                print("Invalid Choice!")

if __name__ == "__main__":
    main()