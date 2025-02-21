import sqlite3

conn = sqlite3.connect("movieCollection.db")
cursor = conn.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS movieCollection (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                release_year INTEGER NOT NULL,
                category TEXT NOT NULL,
                duration INTEGER NOT NULL
                )
        ''')

def list_all_movie():
    cursor.execute("SELECT * FROM movieCollection")
    print("=" * 50)
    for movie in cursor.fetchall():
        print("*" * 30)
        print(f"index: {movie[0]} \nname: {movie[1]} \nRelease Year: {movie[2]} \nCategory: {movie[3]} \nduration: {movie[4]}")
        print("*" * 30)
    conn.commit()
    print("=" * 50)

def add_movie():
    print("=" * 50)
    name_str = input("Enter a movie name: ")
    name = name_str.lower()
    release_year = int(input("Enter a movie release year: "))
    category = input("Enter a movie Category: ").lower()
    duration = int(input("Enter Movie duration(minutes): "))
    cursor.execute("INSERT INTO movieCollection (name,release_year,category,duration) VALUES (?, ?, ?, ?)", (name, release_year, category, duration))
    conn.commit()
    print("=" * 50)

def search_movie():
    name_str = input("Enter a name to search movie: ")
    name = name_str.lower()
    try:
        cursor.execute("SELECT * FROM movieCollection WHERE name = ? ", (name,))
        for detail in cursor.fetchall():
            print("*" * 30)
            print(f"Index: {detail[0]} \nName: {detail[1]} \nRelease Year: {detail[2]} \nCategory: {detail[3]} \nDuration: {detail[4]}")
    finally:
        print("--> movie name incorrect please check spelling, Or movie dose not exists in collection!")

def filter_movie():
    print("1. Filter by Category")
    print("2. Filter by Year")
    option = int(input("Enter Your Filter method: "))

    if option == 1:
        category_name = input("Enter category name: ").lower()
        try:
            cursor.execute("SELECT * FROM movieCollection WHERE category = ?", (category_name,))
            for details in cursor.fetchall():
                print("*" * 30)
                print(f"Index: {details[0]} \nName: {details[1]} \nRelease Year: {details[2]} \nCategory: {details[3]} \nDuration: {details[4]}")
                print("*" * 30)
        finally:
            print("--> Category name incorrect please check spelling, Or Category dose not exists in collection!")

    elif option == 2:
        year = int(input("Enter Release Year: "))
        try:
            cursor.execute("SELECT * FROM movieCollection WHERE release_year = ?", (year,))
            for details in cursor.fetchall():
                print("*" * 30)
                print(f"Index: {details[0]} \nName: {details[1]} \nRelease Year: {details[2]} \nCategory: {details[3]} \nDuration: {details[4]}")
                print("*" * 30)
        finally:
            print("--> Year incorrect, Or Movie dose not exists in collection!")
    else:
        print("Invalid Choice, Please try again!")

def update_movie():
    print("=" * 50)
    list_all_movie()
    movie_id = int(input("Enter movie index: "))
    name_str = input("Enter a new name: ")
    new_name = name_str.lower()
    new_release_year = int(input("Enter new release Year: "))
    new_category = input("Enter a Category: ").lower()
    new_duration = int(input("Enter new Duration: "))
    cursor.execute("UPDATE movieCollection SET name = ?, release_year = ?, category = ?, duration = ? WHERE id = ?", (new_name, new_release_year, new_category, new_duration, movie_id))
    conn.commit()
    print("=" * 50)

def delete_movie():
    print("=" * 50)
    movie_id = int(input("Enter movie index you want to delete: "))
    cursor.execute("DELETE FROM movieCollection WHERE id = ?", (movie_id,))
    print("Movie has been deleted!")
    conn.commit()

def main():
    while True:
        print("=" * 50)
        print("--Movie Collection Manager--")
        print("1. List all Movie Collection")
        print("2. Add Movie")
        print("3. search movie by name: ")
        print("4. filter movie by category or release year: ")
        print("5. Update Movie")
        print("6. Delete Movie")
        print("7. Exit")
        choice = input("Enter Your Choice: ")

        match choice:
            case "1":
                list_all_movie()
            case "2":
                add_movie()
            case "3":
                search_movie()
            case "4":
                filter_movie()
            case "5":
                update_movie()
            case "6":
                delete_movie()
            case "7":
                break
            case __:
                print("Invalid Choice!")
    conn.close


if __name__ == "__main__":
    main()