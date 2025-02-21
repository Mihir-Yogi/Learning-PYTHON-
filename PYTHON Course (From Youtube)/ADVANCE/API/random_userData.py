import requests
import json

def api_handling():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    super_data = response.json()

    if super_data["success"]:
        user_data = super_data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username,country
    else:
        raise Exception("Data was not fatched from api")

def main():
    try:
        username,country = api_handling()
        print(f"Username: {username} \nCountry: {country}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
