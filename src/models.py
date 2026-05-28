from datetime import datetime
import json


class Expense:
    def __init__(self, id: int = None, description: str = None, amount: float = None, date: str = None):
        self.id = _get_last_id() + 1 if not id else id
        self.description = description
        self.amount = amount
        self.created_at = date if date else str(datetime.now())
        print(f"Expense created: {self.id}")
        with open("src/expenses.json", "r") as file:
            data = json.load(file)
            data.append(self.__dict__)
        with open("src/expenses.json", "w") as file:
            json.dump(data, file)


def get_expenses(month: str = None) -> list[Expense]:
    with open("src/expenses.json", "r") as file:
        data = json.load(file)
        expenses = [Expense(**item) for item in data]
        if month:
            expenses = [
                expense
                for expense in expenses
                if expense.created_at.strftime("%Y-%m") == month
            ]
        return expenses


def _get_last_id() -> int:
    with open("src/expenses.json", "r") as file:
        data = json.load(file)
        if data:
            return max(expense.id for expense in [Expense(**item) for item in data])
        return 0


def delete_expense(id: int) -> None:
    copy = [expense for expense in get_expenses() if expense.id != id]
    with open("src/expenses.json", "w") as file:
        json.dump([expense.__dict__ for expense in copy], file)
