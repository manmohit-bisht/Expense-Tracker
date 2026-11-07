import json
from datetime import date
from datetime import datetime
import os
from pathlib import Path

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
    pass


for i in range(3):
    add_expense()
