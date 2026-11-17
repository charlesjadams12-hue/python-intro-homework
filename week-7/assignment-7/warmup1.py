
path = "../data/notes.txt"

with open(path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
        new_line = line.strip()   
        print(f"Line {line_number}: {new_line}") 
    