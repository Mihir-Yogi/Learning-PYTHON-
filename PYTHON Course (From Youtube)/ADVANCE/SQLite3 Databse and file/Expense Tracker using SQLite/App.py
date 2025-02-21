import sqlite3

conn = sqlite3.connect("ExpenseTracker.db")

cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                amount TEXT NOT NULL,
                category TEXT NOT NULL,
                date DATETIME DEFAULT CURRENT_TIMESTAMP
                )
''')

def list_exp():
    cursor.execute("SELECT * FROM expenses")
    for detail in cursor.fetchall():
        print("*" * 30)
        print(f"index: {detail[0]} \nAmount: {detail[1]} \nCategory: {detail[2]} \nDate: {detail[3]}")
        print("*" * 30)

def add_exp():
    print("=" * 50)
    amount = int(input("Enter Amount: "))
    category = input("Enter Category: ").lower()
    cursor.execute("INSERT INTO expenses (amount, category) VALUES (?, ?)", (amount, category))
    conn.commit()
    print("=" * 50)

def update_exp():
    print("=" * 50)
    list_exp()
    index = int(input("Enter Index for Update: "))
    new_amount = int(input("Enter Amount: "))
    new_category = input("Enter Category: ").lower()
    cursor.execute("UPDATE expenses SET amount = ?, category =?, date = CURRENT_TIMESTAMP WHERE id = ? ", (new_amount, new_category, index))
    conn.commit()
    print("=" * 50)

def delete_exp():
    list_exp()
    choice = int(input("Enter Index to Delete: "))
    try:
        cursor.execute("DELETE FROM expenses WHERE id = ? ", (choice,))
        conn.commit()
    finally:
        print("Invalid Index!")
    print("=" * 50)

def summery_report():
    pass

def main():
    while True:
        print("=" * 50)
        print("1. list Expenses")
        print("2. Add Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Summary Report")
        print("6. Exit")
        choice = input("Enter Your Choice: ")

        match choice:
            case "1":
                list_exp()
            case "2":
                add_exp()
            case "3":
                update_exp()
            case "4":
                delete_exp()
            case "5":
                summery_report()
            case "6":
                break
            case __:
                print("Invalid Choice!")
    conn.close()


if __name__ == "__main__":
    main()