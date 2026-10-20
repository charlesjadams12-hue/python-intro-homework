# Error message:
#  File "/Users/charlesadams/Desktop/python_class/CodeTheDream/python-intro-homework/week-2/assignment-2/warmup4.py", line 4
#    print (f"You are {birth year} years old!")
#                      ^^^^^^^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?

# Cause: Undefined variable. 
# Fix: Corrected by adding underscore between "birth" and "year" as defined by the variable.

birth_year = input("What year were you born? ")
birth_year = int(birth_year)
birth_year = 2026 - birth_year
print (f"You are {birth_year} years old!")