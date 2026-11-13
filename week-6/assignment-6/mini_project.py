def show_menu():
        print("\n====== Number Cruncher ======")
        print("1. Find minimum")
        print("2. Find maximum")
        print("3. Search for a number")
        print("4. Sort the list")
        print("5. Quit")
        choice = input("Choose an option (1-5): ")
        return choice

def find_min(numbers): 
            smallest = numbers[0]
    
            for number in numbers:
                if number < smallest:
                    smallest = number
            return smallest
    
def find_max(numbers):
             largest = numbers[0]
     
             for number in numbers:
                 if number > largest:
                     largest = number
             return largest

def search(numbers, target):
             index = -1
    
     
             for i in range(len(numbers)):
                 if numbers[i] == target:
                     index = i
                     break
         
             return index

def bubble_sort(numbers): 
                 numbers_copy = []
                 for number in numbers:
                       numbers_copy.append(number)
                 swapped = True
         
                 while swapped:
                     swapped = False
         
                     for i in range(len(numbers_copy) - 1):
                         if numbers_copy[i] > numbers_copy[i + 1]:
                              numbers_copy[i], numbers_copy[i + 1] = numbers_copy[i + 1], numbers_copy[i]
                              swapped = True
                 return numbers_copy

def goodbye():
             print("Goodbye")
     
     






def main():
    numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
    while True:
        choice = show_menu()

        if choice == "1":
            smallest = find_min(numbers)
            print(f"The minimum value is {smallest}")
        
        elif choice == "2":
            largest = find_max(numbers)
            print(f"The maximum value is {largest}")
        
        elif choice == "3":
                
            try: 
                target = int(input("Enter a number:"))

                index = search(numbers, target)
                
                if index > -1:
                    print(f"Found '{target}' at index {index}.")
                
                else:
                    print(f"'{target}' was not found.")
            
            except ValueError:
                print("Please enter a valid integer")

        elif choice == "4":
            numbers_copy = bubble_sort(numbers)
            print(numbers_copy)
            
        elif choice == "5":
            goodbye()
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()