import json
import os
file_name = 'expenses.json'
def load_expenses():
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    return []
def save_expenses(expenses):
    with open(file_name, 'w') as file:
        json.dump(expenses, file, indent=4)
def add_expense(expenses):
    try:
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        expense = {
            'date': date,
            'category': category,
            'amount': amount,
            'description': description
        }
        expenses.append(expense)
        print("Expense added successfully.")
    except Exception as e:
        print(f"Error adding expense: {e}")
def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. Date: {expense['date']}, Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")
def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")
main()