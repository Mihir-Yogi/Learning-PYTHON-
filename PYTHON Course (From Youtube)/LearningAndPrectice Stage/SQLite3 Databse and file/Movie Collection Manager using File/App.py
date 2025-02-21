import json 

super_file = "movieCollection.txt"

def load_data():
    try:
        with open(super_file,'r') as file:
            result = json.load(file)
            return result
    except:
        return []

def movieHelper(details):
    with open(super_file, 'w') as text:
        json.dump(details, text)

def list_all_movies(details):
    for index,detail in enumerate(details,start=1):
        print("*" * 30)
        print(f"index: {index} \nName: {detail['name']} \nRelease Year: {detail['release_year']} \nCategory: {detail['category']} \nDuration: {detail['duration']}")
        print("*" * 30)

def add_movie(details):
    print("=" * 50)
    name = input("Enter Movie name: ").lower()
    release_year = int(input("Enter movie release year: "))
    category = input("Enter Category: ").lower()
    duration = input("Enter video Duration(minutes): ")
    details.append({"name" : name, "release_year" : release_year, "category" : category, "duration" : duration})
    movieHelper(details)
    print("=" * 50)

def search_movie(details):
    print("=" * 50)
    name = input("Enter Name of movie to search: ").lower()
    for index,detail in enumerate(details,start=1):
        if detail["name"] ==  name:
            print("*" * 30)
            print(f"Index: {index} \nName: {detail["name"]} \nRelease Year: {detail["release_year"]} \nCategory: {detail["category"]} \nDuration: {detail["duration"]}")
            print("*" * 30)

    print("=" * 50)

def filter_movie(details):
    print("=" * 50)
    print("1. Filter by Category")
    print("2. Filter by Release Year")
    choice = int(input("Enter Your choice: "))

    if choice == 1:
        category = input("Enter Category name: ").lower()
        for index,detail in enumerate(details, start=1):
            if detail["category"] == category:
                print("*" * 30)
                print(f"Index: {index} \nName: {detail["name"]} \nRelease Year: {detail["release_year"]} \nCategory: {detail["category"]} \nDuration: {detail["duration"]}")
                print("*" * 30)
    elif choice == 2:
        Year = int(input("Enter Release Year: "))
        for index,detail in enumerate(details, start=1):
            if detail["release_year"] == Year:
                print("*" * 30)
                print(f"Index: {index} \nName: {detail["name"]} \nRelease Year: {detail["release_year"]} \nCategory: {detail["category"]} \nDuration: {detail["duration"]}")
                print("*" * 30)
    else:
        print("*" * 30)
        print("Invalid Choice, Please try again!")
        print("*" * 30)

    print("=" * 50)

def update_movie(details):
    list_all_movies(details)
    index = int(input("Enter index you want to Update: "))
    if 1 <= index <= len(details):
        new_name = input("Enter new name: ").lower()
        new_release_year = int(input("Enter release year: "))
        new_category = input("Enter new Category: ").lower()
        new_duration = int(input("Enter new Duration: "))
        details[index-1] = {'name': new_name, 'release_year': new_release_year, 'category': new_category, 'duration': new_duration}
        movieHelper(details)
    else:
        print("Wrong Index, Plese try again!")

def delete_movie(details):
    list_all_movies(details)
    index = int(input("Enter index you want to delete: "))
    if 1 <= index <= len(details):
        del(details[index-1])
        movieHelper(details)
    else:
        print("Wrong Index, Please try again!")

def main():
    while True:
        details = load_data()
        print("=" * 50)
        print("--Movie Collection Manager--")
        print("1. List all Movie Collection")
        print("2. Add Movie")
        print("3. Search Movie by name")
        print("4. Filter movie")
        print("5. Update Movie")
        print("6. Delete Movie")
        print("7. Exit")
        choice = input("Enter Your Choice: ")

        match choice:
            case "1":
                list_all_movies(details)
            case "2":
                add_movie(details)
            case "3":
                search_movie(details)
            case "4":
                filter_movie(details)
            case "5":
                update_movie(details)
            case "6":
                delete_movie(details)
            case "7":
                break
            case __:
                print("Invalid Choice!")

if __name__ == "__main__":
    main()