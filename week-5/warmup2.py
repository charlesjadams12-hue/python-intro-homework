# Initializing value for while loop.
number = 0
while number <= 0:

# Handles any non-numeric inputs and floats.
    try: 
        number = int(input("Enter a positive integer: "))

    except ValueError:
        print("That isn't an integer. Try again.")
        continue
    
# Creating condition for loop to end.
    if number > 0:
            print(f"Got it: {number}")
            break
    
# Handles any other input conditions including negative numbers.
    else:
         print(f"That is not a positive integer. Please try again.")
  
        