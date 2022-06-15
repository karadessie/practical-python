print("Welcome!")
name = input("What is your name?\n")
print("choose a number between 1 and 100\n")
computers_number = 75

def compare():
    guess = input("What is your guess?\n")
    int_guess = int(guess)
    if int_guess > computers_number:
        print("Your guess is too high, try again")
        compare()
    elif int_guess < computers_number:   
        print("Your guess is too low, try again")
        compare()
    else:
        print("Congratulations " + name + "!")

compare()