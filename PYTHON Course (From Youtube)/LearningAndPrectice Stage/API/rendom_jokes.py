import requests
import json

def api_handling():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = requests.get(url)
    super_data = response.json()

    if super_data["success"]:
            data = super_data["data"]
            random_joke = data['content']
            print("*" * 30)
            print(random_joke)
            print("*" * 30)
    else:
        raise Exception("Data dose not Fatched!")
    

def main():
    count = 0
    while True:
        print("=" * 50)
        if count == 0 : 
            print("1. Start")
            count += 1
        else: 
            print("1. One more")
        print("2. Exit")
        choice = input("Enter Your Choice: ")
        match choice:
            case "1":
                api_handling()
            case "2":
                break
            case __:
                print("Invalid Choice.")


if __name__ == "__main__":
    main()
