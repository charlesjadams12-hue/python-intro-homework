age = int(input("How old are you? "))
if age >= 0 and age < 13: 
    print(f"You are considered to be a child.")
elif age >= 13 and age < 18: 
    print(f"You are considered to be a teenager")
elif age >= 18 and age < 65:
    print(f"You are considered to be an adult")
elif age >= 65:
    print(f"You are considered to be a senior citizen")
else:
    print(f"Invalid age. Please try again.")