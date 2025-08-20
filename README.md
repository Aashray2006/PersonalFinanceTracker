💰 Simple Personal Finance Tracker (Python)
This is a console-based personal finance tracker written in Python. It's designed to help you easily manage and monitor your income and expenses. The application saves your financial data to a file, so your records are preserved between sessions.

⚙️ Key Features
Transaction Management: Add, view, and track both income and expenses.

Data Persistence: All transactions are automatically saved to and loaded from a finance_data.json file.

Financial Summary: Get a quick overview of your total income, total expenses, and net savings.

Search & Filter: Find specific transactions by searching for a keyword in the description or by filtering for expenses over a certain amount.

Visual Chart: Visualize your monthly spending with a simple ASCII bar chart.

🚀 How to Run
Prerequisites
Ensure you have Python 3.x installed on your system.

Execution
Save the code provided in the previous response into a file named finance_tracker.py.

Open your terminal or command prompt.

Navigate to the directory where you saved the file.

Run the application using the following command:

Bash

python finance_tracker.py
Follow the on-screen menu to interact with the finance tracker.

📋 Sample Output
When you run the application for the first time, it will load an empty list.

No data file found (finance_data.json). Starting with a new, empty list.

--- Main Menu ---
1. Add Income
2. Add Expense
3. View All Transactions
4. View Financial Summary
5. Search & Filter Transactions
6. View Monthly Expense Chart
7. Exit
Enter your choice: 2

--- Add Expense ---
Enter amount: $50.00
Enter description: Dinner with friends
Enter date (YYYY-MM-DD, press Enter for today): 2025-08-15
Expense added successfully!
Data saved successfully to finance_data.json

--- Main Menu ---
1. Add Income
2. Add Expense
3. View All Transactions
4. View Financial Summary
5. Search & Filter Transactions
6. View Monthly Expense Chart
7. Exit
Enter your choice: 1

--- Add Income ---
Enter amount: $1500.00
Enter description: Monthly salary
Enter date (YYYY-MM-DD, press Enter for today): 2025-08-01
Income added successfully!
Data saved successfully to finance_data.json

--- Main Menu ---
1. Add Income
2. Add Expense
3. View All Transactions
4. View Financial Summary
5. Search & Filter Transactions
6. View Monthly Expense Chart
7. Exit
Enter your choice: 4

--- Financial Summary ---
Total Income:  $1500.00
Total Expenses: $50.00
Net Savings:   $1450.00

--- Main Menu ---
1. Add Income
2. Add Expense
3. View All Transactions
4. View Financial Summary
5. Search & Filter Transactions
6. View Monthly Expense Chart
7. Exit
Enter your choice: 7
Goodbye!
