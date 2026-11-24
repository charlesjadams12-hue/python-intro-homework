while True:
    try: 
        user_input = float(input("Enter a number: "))

    except ValueError:
        print(f"That's not a valid number. Try again.")

    else:
        print(f"You entered: {user_input}")
        break
        