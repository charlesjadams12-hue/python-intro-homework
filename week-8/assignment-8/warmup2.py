while True:
    try: 
        numerator = float(input("Enter a numerator: "))
        denominator = float(input("Enter a denominator: "))
        answer = numerator / denominator

    except ValueError:
        print(f"Can't divide by non-numerical elements")

    except ZeroDivisionError:
        print(f"Can't divide by zero. Please enter a number greater or lesser than zero.")

    else:
        print(f"{numerator} ÷ {denominator} = {answer}")
        break