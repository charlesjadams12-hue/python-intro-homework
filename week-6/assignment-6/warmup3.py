def user_name():
    name = "John"
    return name # Removing this line would result in None.

# Example showing local scope.

# print(name) 
# NameError: name 'name' is not defined).


# Using return and correctly way to assigning variable to outer scope.
name = user_name()
print (name)