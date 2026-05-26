# Expense Tracker

A simple command-line expense tracker to help you add, update, delete, and view expenses, and to produce summaries (total and monthly).

## Features

- Add an expense with a description and amount.
- Update an existing expense.
- Delete an expense by ID.
- List all expenses.
- Show a summary (total) of expenses.
- Show a summary for a specific month (current year).

Optional features you can add:

- Categories and filtering by category.
- Per-month budgets and warnings when exceeded.
- Export / import to CSV.

## Quick Start (Recommended: Python)

Prerequisites:

- Python 3.8+

Installation (example using a script named `expense-tracker`):

1. Create a virtual environment (optional):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Create a small script `expense-tracker` (or `expense_tracker.py`) and make it executable, or install as a console script.

Data storage:

- Expenses can be stored in a JSON file (e.g. `expenses.json`) in the project folder or a user data directory.

## Data model

Each expense can be stored as an object with these fields:

```json
{
  "id": 1,
  "date": "2024-08-06",
  "description": "Lunch",
  "amount": 20.0,
  "category": "Food" // optional
}
```

IDs should be unique integers (auto-increment).

## CLI: Commands & Usage

Examples (bash):

```bash
$ expense-tracker add --description "Lunch" --amount 20
# Expense added successfully (ID: 1)

$ expense-tracker add --description "Dinner" --amount 10
# Expense added successfully (ID: 2)

$ expense-tracker list
# ID  Date       Description  Amount
# 1   2024-08-06  Lunch        $20.00
# 2   2024-08-06  Dinner       $10.00

$ expense-tracker summary
# Total expenses: $30.00

$ expense-tracker delete --id 2
# Expense deleted successfully

$ expense-tracker summary
# Total expenses: $20.00

$ expense-tracker summary --month 8
# Total expenses for August: $20.00
```

Common commands and flags (suggested):

- `add --description <text> --amount <number> [--category <name>]`
- `update --id <id> [--description <text>] [--amount <number>] [--category <name>]`
- `delete --id <id>`
- `list [--month <num>] [--category <name>]`
- `summary [--month <num>] [--category <name>]`
- `export --file expenses.csv` (optional)

## Implementation Notes & Tips

- Use a command-line parser (e.g., Python's `argparse` or `click`) to build the CLI.
- Store data in `expenses.json` as a list of expense objects. Load at startup and write back on changes.
- Use ISO date format (`YYYY-MM-DD`) for dates. Default to today's date when adding an expense.
- Validate inputs: amounts must be positive numbers; IDs must exist before updating/deleting.
- When computing monthly summaries, use the expense `date` year to filter to the current year (or accept a `--year` flag).
- Keep file operations atomic: write to a temp file then rename to avoid data corruption.

```python
# example: expense_tracker.py (sketch)
import argparse
import json
from datetime import date

DATA_FILE = 'expenses.json'

def load():
	try:
		with open(DATA_FILE, 'r') as f:
			return json.load(f)
	except FileNotFoundError:
		return []

def save(expenses):
	with open(DATA_FILE, 'w') as f:
		json.dump(expenses, f, indent=2)

# Implement add/list/update/delete/summary using argparse and these helpers.
```

## Testing & Run

- Run the script directly: `python expense_tracker.py <command> ...` or create an executable `expense-tracker` wrapper.
- For development, run manual scenarios matching the examples above.

Inspired by: https://roadmap.sh/projects/expense-tracker

