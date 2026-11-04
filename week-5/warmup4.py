# Create loop of number 1-30.
for number in range(1,31):

# Checks if numbers are divisible by 3 and 5 first.
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

# Checks if numbers are divisible by 3.
    elif number % 3 == 0:
        print("Fizz")

# Checks if numbers are divisible by 5.
    elif number % 5 == 0:
        print("Buzz")

# Prints number if not divisible by 3 or 5.
    else:
        print(number)