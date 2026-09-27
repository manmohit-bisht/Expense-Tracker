import json
from datetime import date
from datetime import datetime
import os

ID = 0 + 1


class Bill_class:
    def __init__(self, amount: int, category: str, description: str, pay_date: str):
        self.expense = {
            "ID": ID,
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

    bill_obj = Bill_class(amount, category, description, valid_date)

    with open("expense.json", "r") as file:
        expense_list = json.load(file)

    expense_list.append(bill_obj.expense)
    with open("expense.json", "w") as file:
        json.dump(expense_list, file, indent=2)


def view_expense():
    pass


for i in range(3):
    add_expense()
