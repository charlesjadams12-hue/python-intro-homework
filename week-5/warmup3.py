names = ["John", "Marcus", "Molly", "Sandra", "Michael"]

target = input("Enter a name to search for: ")

index = -1

for i in range(len(names)):
    if names[i] == target:
        index = i
        break
if index > -1:
    print(f"Found '{target}' at index {index}.")
else:
    print(f"'{target}' was not found.")
