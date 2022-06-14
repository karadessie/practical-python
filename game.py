print("Welcome!")
name = input("What is your name?\n")
print("choose random number between 1 and 100\n")
guess = input("What is your guess?\n")
numguess = 50
number = 75
    
if guess > number:
        print("Your guess is too high, try again")
        numguess = numguess + 1
if guess < number:   
        print("Your guess is too low, try again")
        numguess = numguess + 1
else:
        print("Congratulations " + name + "!")