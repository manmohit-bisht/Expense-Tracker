# Expense Tracker

# Expense Tracker CLI

Keep everyday spending visible, organized, and easier to manage. **Expense Tracker** is a lightweight command-line app for recording expenses and reviewing or maintaining them whenever you need to.

## Why I Built This
I built this simple project because I kept losing track of my UPI and cash expenses turns out "just a quick ₹15 chai" adds up faster than memory leaks(😅 a bit hypocritical to say while coding in Python, but you get my point) and wanted a keyboard-first way to log them straight from the terminal without opening any bloated software. It really helps when I'm sitting in a cafeteria working—if I buy something, I can log the expense directly from my terminal without having to distrupt my workflow.

## Features
* Fast, keyboard-first CLI workflow
* Persistent local JSON storage (`expense.json`)
* Clean formatted summary tables powered by `tabulate`

## Set up

You’ll need Python 3.8 or newer.

1. Clone the repository and move into the project directory:

   ```powershell
   git clone https://github.com/manmohit-bisht/Expense-Tracker.git
   cd Expense-Tracker
   ```
2. Install the project in editable mode:

   ```powershell
   pip install -e .
   ```

   The project requires `tabulate` (version 0.8.9 or newer) to format expense lists. Because it is declared as a project dependency, `pip install -e .` installs it automatically along with the `exptracker` command. Editable mode points the command at this checkout, so changes to the project take effect without reinstalling it.

   If `pip` isn't recognized, use the Python launcher instead:

   ```powershell
   py -m pip install -e .
   ```

## Run it

After installation, launch the app from a terminal:

```powershell
exptracker
```

The command is registered with the Python environment used during installation. With a system-wide Python installation whose Scripts directory is on your `PATH`, you can run `exptracker` from any terminal and any working directory. If you installed it in a virtual environment, activate that environment first; its command is available while it’s active.

The app opens an interactive menu:

```text
Expense Tracker Menu:
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Exit
```

Choose an option and follow the prompts. When adding an expense, enter the date as `DD-MM-YYYY` (for example, `12-05-2026`). You can leave update fields blank to keep their existing values.

## Your expense data

Expenses are stored locally as JSON in `src/expense.json`; no account or external service is needed. Keep a backup of this file if the records matter to you. Since the data file lives inside the project installation, take care when removing or replacing that checkout.

## A small tool, built for the command line

The goal is straightforward: make it quick to record an expense, then make it just as easy to see and manage what you've recorded. The app keeps the workflow in your terminal and the data in a file you can inspect and back up yourself.
