students = {"name": "John", "grade": 55, "subjects": ["Math", "English", "Science"]}
# Prints key values.
for keys, values in students.items():
    print(f"{keys}: {values}")
# Adding graduated key value.
students["graduated"] = False
# Printing updated dictionary.
print(students)