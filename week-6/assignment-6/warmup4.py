def is_valid_score(score):
    """Function used to evaluate range of valid scores."""
    if score >= 0 and score <= 100:
       return True
    else: 
        return False


def main():
    """Takes user input and with conditional decides output."""
    score = int(input("What is your score? "))
    if is_valid_score(score):
        print("Valid score")
    else:
        print("Invalid score - must be between 0 and 100")
   

if __name__ == "__main__":
    main()
