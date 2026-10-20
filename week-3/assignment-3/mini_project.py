day = input("What day is it? ").lower()
time = input("Is it the morning, afternoon, or evening? ").lower()
if day == "wednesday":
    if time == "morning":
        print(f"Suggestion: You should probably get ready for work.")
    elif time == "afternoon":
        print(f"Suggestion: You should go to the new Mexican restaurant for your lunch break.")
    elif time == "evening":
        print(f"Suggestion: A quiet evening inside would be nice.")
    else:
        print(f"Can't recognize that time. Try morning, afternoon, evening....")
elif day == "friday": 
    if time == "morning":
        print(f"Suggestion: You have a doctor's appointment. Make sure to leave 30 minutes before.")
    elif time == "afternoon":
        print(f"Suggestion: You have a Python class - make sure to study before")
    elif time == "evening":
        print(f"Suggestion: Go out and enjoy your weekend!")
    else: 
        print(f"Can't recognize that time. Try morning, afternoon, evening....")
elif day == "sunday":
    if time == "morning":
        print(f"Suggestion: Get some extra sleep.")
    elif time == "afternoon":
        print(f"Suggestion: Good time to cut the grass")
    elif time == "evening":
        print(f"Suggestion: Try reading before going to bed")
    else:
        print(f"Can't recognize that time. Try morning, afternoon, evening....")
else: 
    print(f"Sorry I do not recognize that day or you don't have anything going on during that period of time.")
