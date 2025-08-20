import json
from datetime import datetime
import os

DATA_FILE = "finance_data.json"

class FinanceTracker:
    def __init__(self):
        self.transactions = []
        self.load_data()

    def _save_data(self):
        try:
            with open(DATA_FILE, 'w') as f:
                json.dump(self.transactions, f, indent=4)
            print(f"\nData saved successfully to {DATA_FILE}")
        except IOError:
            print(f"\nError: Could not save data to {DATA_FILE}")

    def load_data(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, 'r') as f:
                    self.transactions = json.load(f)
                print(f"\nData loaded successfully from {DATA_FILE}")
            except (IOError, json.JSONDecodeError):
                print(f"\nError: Could not load data from {DATA_FILE}. Starting with an empty list.")
                self.transactions = []
        else:
            print(f"\nNo data file found ({DATA_FILE}). Starting with a new, empty list.")

    def add_transaction(self, transaction_type):
        print(f"\n--- Add {transaction_type.capitalize()} ---")
        try:
            amount = float(input("Enter amount: $"))
            description = input("Enter description: ")
            date_str = input("Enter date (YYYY-MM-DD, press Enter for today): ")
            
            if not date_str:
                date_str = datetime.now().strftime("%Y-%m-%d")
            else:
                datetime.strptime(date_str, "%Y-%m-%d")

            transaction = {
                "date": date_str,
                "type": transaction_type,
                "amount": amount,
                "description": description
            }
            self.transactions.append(transaction)
            print(f"{transaction_type.capitalize()} added successfully!")
            self._save_data()
        except ValueError:
            print("Invalid input. Please enter a valid number for the amount and a valid date format.")

    def view_all_transactions(self):
        if not self.transactions:
            print("\nNo transactions recorded yet.")
            return

        print("\n--- All Transactions ---")
        print("{:<12} {:<10} {:<15} {:<30}".format("Date", "Type", "Amount", "Description"))
        print("-" * 67)
        for t in self.transactions:
            amount_str = f"${t['amount']:.2f}"
            print("{:<12} {:<10} {:<15} {:<30}".format(t['date'], t['type'].capitalize(), amount_str, t['description']))

    def get_summary(self):
        total_income = sum(t['amount'] for t in self.transactions if t['type'] == 'income')
        total_expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')
        net_savings = total_income - total_expenses
        
        print("\n--- Financial Summary ---")
        print(f"Total Income:  ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Net Savings:   ${net_savings:.2f}")

    def filter_transactions(self):
        print("\n--- Search and Filter ---")
        choice = input("Filter by (1) Keyword in description or (2) Expenses over a certain amount? (Enter 1 or 2): ")
        
        if choice == '1':
            keyword = input("Enter a keyword to search for: ").lower()
            filtered_list = [t for t in self.transactions if keyword in t['description'].lower()]
            print("\n--- Filtered Results (by keyword) ---")
        elif choice == '2':
            try:
                min_amount = float(input("Enter the minimum expense amount: $"))
                filtered_list = [t for t in self.transactions if t['type'] == 'expense' and t['amount'] >= min_amount]
                print(f"\n--- Filtered Results (Expenses >= ${min_amount:.2f}) ---")
            except ValueError:
                print("Invalid amount. Please enter a number.")
                return
        else:
            print("Invalid choice.")
            return

        if not filtered_list:
            print("No matching transactions found.")
            return
            
        print("{:<12} {:<10} {:<15} {:<30}".format("Date", "Type", "Amount", "Description"))
        print("-" * 67)
        for t in filtered_list:
            amount_str = f"${t['amount']:.2f}"
            print("{:<12} {:<10} {:<15} {:<30}".format(t['date'], t['type'].capitalize(), amount_str, t['description']))

    def _get_monthly_expenses(self):
        monthly_expenses = {}
        for t in self.transactions:
            if t['type'] == 'expense':
                month_year = datetime.strptime(t['date'], "%Y-%m-%d").strftime("%Y-%m")
                monthly_expenses[month_year] = monthly_expenses.get(month_year, 0) + t['amount']
        return monthly_expenses

    def show_monthly_chart(self):
        monthly_data = self._get_monthly_expenses()
        if not monthly_data:
            print("\nNo expenses recorded to generate a chart.")
            return
        
        print("\n--- Monthly Expense Chart ---")
        sorted_months = sorted(monthly_data.keys())
        
        max_amount = max(monthly_data.values())
        if max_amount == 0:
            print("No expenses to chart.")
            return

        bar_length = 50
        
        for month in sorted_months:
            amount = monthly_data[month]
            bar = '█' * int(bar_length * (amount / max_amount))
            print(f"{month}: {bar} ${amount:.2f}")

    def run(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View All Transactions")
            print("4. View Financial Summary")
            print("5. Search & Filter Transactions")
            print("6. View Monthly Expense Chart")
            print("7. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.add_transaction('income')
            elif choice == '2':
                self.add_transaction('expense')
            elif choice == '3':
                self.view_all_transactions()
            elif choice == '4':
                self.get_summary()
            elif choice == '5':
                self.filter_transactions()
            elif choice == '6':
                self.show_monthly_chart()
            elif choice == '7':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = FinanceTracker()
    app.run()
