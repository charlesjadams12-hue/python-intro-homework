name = "Alex"

def greet(name, greeting="Hello"): 
    print(f"{greeting}, {name}!")

# Calling function just using name.
greet(name)

# Calling function with a custom greeting.
greet(name, "Good morning, I hope you have a special day")

# Calling function using keywords.
greet(name="Alex", greeting="Good evening")