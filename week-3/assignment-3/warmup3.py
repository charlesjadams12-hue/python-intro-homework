print(not True and False)  # Prints False, not True equals False; False and False results in False.
print(True or False and False) # Prints True, because of operator precedence (False and False) is evaluated firstand equals false; then True or False results in True.
print(not (5 > 3)) # Prints False, 5 > 3 is a true statement; the "not" operator inverts it to False.
print(10 == 10 and 4 != 4) # Prints False, 10 == 10 is a true statement; while 4 != 4 is a false statement; True and False results in False.
print(not False or not True) # Prints True, not False equals True; not True equals False; True or False equals True.