path = "../data/missing.txt"

try: 
    with open(path, "r") as file:
        file.read()
except FileNotFoundError:
    print(f"Error: {path} was not found. Please check the file path and try again.")