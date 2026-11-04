numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    print("\n====== Number Cruncher ======")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")

# Finding minimum
    if choice == "1": 
        smallest = numbers[0]

        for number in numbers:
            if number < smallest:
                smallest = number
        print(f"The minimum value is {smallest}")

    if choice == "2":
        largest = numbers[0]

        for number in numbers:
            if number > largest:
                largest = number
        print(f"The maximum value is {largest}")

    if choice == "3": 
        index = -1
        target = int(input("Enter a number:"))

        for i in range(len(numbers)):
            if numbers[i] == target:
                index = i
                break
    
        if index > -1:
            print(f"Found '{target}' at index {index}.")
        else:
            print(f"'{target}' was not found.")

    if choice == "4":
            swapped = True
    
            while swapped:
                swapped = False
    
                for i in range(len(numbers) - 1):
                    if numbers[i] > numbers[i + 1]:
                         numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                         swapped = True
            print(numbers)
   
    if choice == "5":
        print("Goodbye")
        break


