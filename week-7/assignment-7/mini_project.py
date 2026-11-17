import os
import csv
from datetime import datetime

path = "../data/expenses.csv"

if os.path.exists(path):
    with open(path, 'r') as file:
        records = list(csv.DictReader(file))
        
        for row in records:
            
            row["amount"] = float(row["amount"])
            
        food_expenses = []
            
        for row in records:
            if row["category"] == "Food":
                food_expenses.append(row)

        total_cost = 0
            
        for expense in food_expenses:
            total_cost += expense["amount"]
            
        today = datetime.now().strftime("%B %d, %Y")     

        with open("food_report.txt", "w") as report:
            report.write(f"Food Expense Report — generated {today}\n")
            for expense in food_expenses:
                report.write(f"{expense["date"]}: ${expense["amount"]:.2f}\n")
            report.write(f"Total: ${total_cost:.2f}\n")

else:
    print("Error: expenses.csv was not found.")