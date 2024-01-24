import sqlite3
from datetime import datetime

def create_expense_table():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            category TEXT,
            description TEXT,
            date TEXT
        )
    ''')

    conn.commit()
    conn.close()

def add_expense(amount, category, description):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO expenses (amount, category, description, date) VALUES (?, ?, ?, ?)",
                   (amount, category, description, date))

    conn.commit()
    conn.close()

def view_expenses():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    if expenses:
        print("Expenses:")
        for expense in expenses:
            print(f"{expense[4]} - ${expense[1]} ({expense[2]}): {expense[3]}")
    else:
        print("No expenses recorded.")

    conn.close()

def main():
    create_expense_table()

    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            amount = float(input("Enter the expense amount: "))
            category = input("Enter the expense category: ")
            description = input("Enter a short description: ")
            add_expense(amount, category, description)
            print("Expense added successfully.")
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
