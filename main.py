import argparse
from src.models import Expense, get_expenses, delete_expense

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    add_parser = subparsers.add_parser("add", help="Add new expense")
    delete_parser = subparsers.add_parser("delete", help="Delete an expense")
    list_parser = subparsers.add_parser("list", help="List all expenses")
    summary_parser = subparsers.add_parser("summary", help="Show expense summary")

    add_parser.add_argument("--description", type=str, help="Description of the expense")
    add_parser.add_argument("--amount", type=float, help="Amount of the expense")

    delete_parser.add_argument("--id", type=int, help="ID of the expense to delete")

    summary_parser.add_argument("--month", type=str, help="Month for summary (e.g., '2024-06')")
    
    args = parser.parse_args()
    if args.command == "add":
        if args.description and args.amount:
            Expense(description=args.description, amount=args.amount)
        else:
            print("Please provide both description and amount for the expense.")
    elif args.command == "delete":
        if args.id:
            delete_expense(id=args.id)
        else:
            print("Please provide the ID of the expense to delete.")
    elif args.command == "list":
        expenses = get_expenses()
        for expense in expenses:
            print(f"ID: {expense.id}, Description: {expense.description}, Amount: {expense.amount}, Created At: {expense.created_at}")
    elif args.command == "summary":
        expenses = get_expenses(month=args.month)
        total = sum(expense.amount for expense in expenses)
        print(f"Month: {args.month}, Total Expenses: {total}")
    else:
        parser.print_help()
if __name__ == "__main__":
    main()
