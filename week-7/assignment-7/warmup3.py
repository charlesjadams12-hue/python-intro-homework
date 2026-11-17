import os

current_directory = os.getcwd()
print(current_directory)

if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

path = os.path.join("..", "data", "expenses.csv")

print(path)