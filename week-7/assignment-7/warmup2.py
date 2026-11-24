import csv

path = "../data/students.csv"

with open(path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['name']}: {row['score']}")
