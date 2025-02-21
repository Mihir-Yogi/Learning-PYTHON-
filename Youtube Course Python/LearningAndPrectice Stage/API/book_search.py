import requests
import json

def api_handling():
    url = "https://api.freeapi.app/api/v1/public/books?page=1&limit=10&inc=kind%2Cid%2Cetag%2CvolumeInfo&query=tech"
    response = requests.get(url)
    super_data = response.json()
    if super_data["success"]:
        data = super_data["data"]
        books_collection = data["data"]
        return books_collection
    else:
        raise Exception("Data dose not fetched!")

def search_books(books_List):
    title = input("Enter title of Book: ").lower()
    found = False
    for book in books_List:
        book_title = (book["volumeInfo"]["title"]).lower()
        if book_title == title:
            title = book["volumeInfo"]["title"]
            author = book["volumeInfo"]["authors"][0]
            year = book["volumeInfo"]["publishedDate"]
            found += True
            print("*" * 30)
            print(f"Book Title: {title} \nAuthor: {author} \nPublish Year: {year}")
            print("*" * 30)

            answer = input("You Want to read Description of this book(Y/N): ")
            if answer == "Y" or answer == "y":
                print(book["volumeInfo"]["description"])
            else:
                break
    if found != True:
        print("--> Book not found!")

def list_all_books(books_list):
    totle_books = 0
    for book in books_list:
        title = book["volumeInfo"]["title"]
        author = book["volumeInfo"]["authors"][0]
        year = book["volumeInfo"]["publishedDate"]
        totle_books += 1
        print("*" * 30)
        print(f"Book Title: {title} \nAuthor: {author} \nPublish Year: {year}")
        print("*" * 30)
    return totle_books


def main():
    books = api_handling()
    while True:
        print("=" * 50)
        print("1. List all books: ")
        print("2. Search Book by title")
        print("3. Exit")
        choice = input("Enter Your Choice: ")
        print("=" * 50)
        match choice:
            case "1":
                totle_books = list_all_books(books)
                print("=" * 30)
                print(f"Totle Books Available is: {totle_books}")
            case "2":
                search_books(books)
            case "3":
                break
            case __:
                print("Invalid Input!")


if __name__ == "__main__":
    main()