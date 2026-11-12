import json
from datetime import datetime
from pathlib import Path
from tabulate import tabulate

BASE_DIR = Path(__file__).resolve().parent
FILE_PATH = BASE_DIR / "expense.json"


class Bill_class:
    def __init__(self, amount: int, category: str, description: str, pay_date: str):
        self.expense = {
            "ID": 0,
            "Amount": amount,
            "Category": category,
            "Description": description,
            "Date": pay_date,
        }


def add_expense():
    try:
        amount = int(input("Amount: "))
    except ValueError:
        print("Not an integer!!")
        return
    category = input("Category: ")
    description = input("Description: ")

    date_string = input("Date: ")
    try:
        dt_object = datetime.strptime(date_string, "%d-%m-%Y")
        valid_date = str(dt_object.date())

    except ValueError:
        print(f" Invalid! '{date_string}' is not a valid date")
        return

    # creating an object of Bill_class
    bill_obj = Bill_class(amount, category, description, valid_date)

    if not FILE_PATH.exists():
        expense_list = []
    else:
        with open(FILE_PATH, "r") as file:
            expense_list = json.load(file)
    # updating the ID of the expense
    ID = len(expense_list) + 1
    bill_obj.expense["ID"] = ID

    # writing the expense to the file
    expense_list.append(bill_obj.expense)
    with open(FILE_PATH, "w") as file:
        json.dump(expense_list, file, indent=2)


def view_expense():
    if not FILE_PATH.exists():
        print("No expenses found.")
        return

    with open(FILE_PATH, "r") as file:
        expense_list = json.load(file)

    if not expense_list:
        print("No expenses found.")
        return

    headers = ["ID", "Amount", "Category", "Description", "Date"]
    rows = []
    # rows is just a 2d list that will hold all the expenses in a tabular format
    for expense in expense_list:
        rows.append(
            [
                expense["ID"],
                expense["Amount"],
                expense["Category"],
                expense["Description"],
                expense["Date"],
            ]
        )
    print(
        tabulate(
            rows,
            headers=headers,
            tablefmt="rounded_grid",
            maxcolwidths=[5, 10, 15, 25, 12],
        )
    )


def update_expense():
    if not FILE_PATH.exists():
        print("No expenses found.")
        return

    with open(FILE_PATH, "r") as file:
        expense_list = json.load(file)

    if not expense_list:
        print("No expenses found.")
        return

    try:
        expense_id = int(input("Enter the ID of the expense to update: "))
    except ValueError:
        print("Invalid input! Please enter a valid integer ID.")
        return

    # Find the expense with the given ID
    if expense_id > 1 and expense_id <= len(expense_list):
        expense_to_update = expense_list[expense_id - 1]
    else:
        expense_to_update = None

    if not expense_to_update:
        print(f"No expense found with ID {expense_id}.")
        return

    # Prompt user for new values (press Enter to keep current value)
    new_amount = input(f"New Amount (current: {expense_to_update['Amount']}): ")
    new_category = input(f"New Category (current: {expense_to_update['Category']}): ")
    new_description = input(
        f"New Description (current: {expense_to_update['Description']}): "
    )
    new_date_string = input(
        f"New Date (current: {expense_to_update['Date']}, format DD-MM-YYYY): "
    )

    # Update values if provided
    if new_amount:
        try:
            expense_to_update["Amount"] = int(new_amount)
        except ValueError:
            print("Invalid amount! Keeping current value.")

    if new_category:
        expense_to_update["Category"] = new_category

    if new_description:
        expense_to_update["Description"] = new_description

    if new_date_string:
        try:
            dt_object = datetime.strptime(new_date_string, "%d-%m-%Y")
            expense_to_update["Date"] = str(dt_object.date())
        except ValueError:
            print("Invalid date format! Keeping current value.")

    # Write updated expenses back to the file
    with open(FILE_PATH, "w") as file:
        json.dump(expense_list, file, indent=2)

    print(f"Expense with ID {expense_id} has been updated.")


def delete_expense():
    if not FILE_PATH.exists():
        print("No expenses found.")
        return

    with open(FILE_PATH, "r") as file:
        expense_list = json.load(file)

    if not expense_list:
        print("No expenses found.")
        return

    try:
        expense_id = int(input("Enter the ID of the expense to delete: "))
    except ValueError:
        print("Invalid input! Please enter a valid integer ID.")
        return

    # Find the expense with the given ID
    if expense_id > 1 and expense_id <= len(expense_list):
        expense_to_delete = expense_list[expense_id - 1]
    else:
        expense_to_delete = None

    if not expense_to_delete:
        print(f"No expense found with ID {expense_id}.")
        return

    # Remove the expense from the list
    expense_list.remove(expense_to_delete)

    # upadte the IDs of the remaining expenses
    for i in range(expense_id - 1, len(expense_list)):
        expense_list[i]["ID"] -= 1
    # Write updated expenses back to the file
    with open(FILE_PATH, "w") as file:
        json.dump(expense_list, file, indent=2)

    print(f"Expense with ID {expense_id} has been deleted.")


if __name__ == "__main__":
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expense()
        elif choice == "3":
            update_expense()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
