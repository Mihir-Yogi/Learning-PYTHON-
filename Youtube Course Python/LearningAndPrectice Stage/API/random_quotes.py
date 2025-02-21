import requests
import json 

def api_handling():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    response = requests.get(url)
    super_data = response.json()
    if super_data["success"]:
        data = super_data["data"]
        author = data["author"]
        content = data["content"]
        return author,content
    else:
        raise Exception("--> Data dose not fetched!")

def main():
    count = 0
    while True:
        print("=" * 50)
        if count == 0:
            print("1. Start")
            count += 1
        else:
            print('1. One More')
        print("2. Exit")
        choice = int(input("Enter Your Choice: "))
        match choice:
            case 1:
                try:
                    author,content = api_handling()
                    print("*" * 30)
                    print(f"Auther: {author} \nQuote: {content}")
                    print("*" * 30)
                except:
                    print("--> Values dose not returned!")
            case 2:
                break
            case __:
                print("--> Invalid Choice!")

if __name__ == "__main__":
    main()