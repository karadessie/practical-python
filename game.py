print("Welcome!")
name = input("What is your name?\n")
print("choose a number between 1 and 100\n")
guess = input("What is your guess?\n")
num_guesses = 10
computers_number = 75
    
if guess > computers_number:
        print("Your guess is too high, try again")
        num_guesses = num_guesses + 1
elif guess < computers_number:   
        print("Your guess is too low, try again")
        num_guesses = num_guesses + 1
else:
        print("Congratulations " + name + "!")