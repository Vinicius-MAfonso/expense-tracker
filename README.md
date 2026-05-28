# Expense Tracker CLI Application

Build a simple expense tracker application to manage your finances. The application should allow users to add, delete, update, and view their expenses. It should also provide summaries of expenses.

---

## Requirements

The application should run from the command line and support the following features:

* Add an expense with a description and amount
* Update an existing expense
* Delete an expense
* View all expenses
* View a summary of all expenses
* View a summary of expenses for a specific month (of the current year)

---

## Optional Features

You can extend the application with additional functionality such as:

* Add expense categories and filter expenses by category
* Set a monthly budget and display warnings when exceeded
* Export expenses to a CSV file

---

## Example Commands

```bash
$ expense-tracker add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)

$ expense-tracker add --description "Dinner" --amount 10
# Expense added successfully (ID: 2)

$ expense-tracker list
# ID  Date        Description  Amount
# 1   2024-08-06  Lunch        $20
# 2   2024-08-06  Dinner       $10

$ expense-tracker summary
# Total expenses: $30

$ expense-tracker delete --id 2
# Expense deleted successfully

$ expense-tracker summary
# Total expenses: $20

$ expense-tracker summary --month 8
# Total expenses for August: $20
```

---

## Implementation Suggestions

You can implement the application using any programming language of your choice.

### Recommended Approaches

* Use a command-line argument parser:

  * Python: `argparse`
  * Node.js: `commander`
  * Other languages: equivalent CLI libraries

* Store expense data in a simple file format:

  * JSON
  * CSV
  * SQLite (optional upgrade)

---

## Best Practices

* Add proper error handling for:

  * Negative amounts
  * Missing fields
  * Invalid commands
  * Non-existent expense IDs

* Use modular functions/classes to:

  * Improve maintainability
  * Simplify testing
  * Organize business logic

---

## Learning Outcomes

This project is a great way to practice:

* CLI application development
* File system interaction
* Data management
* Argument parsing
* Error handling
* Code organization and modularity
