from random import randint


# Function for Guessing Number
def randomNumberGuesser():
    # Initialise the random variable
    randomNumber = randint(1, 10)
    # Check if the user has guessed the correct number
    guessed = False
    # For loop to iterate each atttempt and provide input, validation and response
    for i in range(3):
        if guessed == False:
            if guessed == False & i != 3:
                Userinput = int(input ("(" + str(i+1) + "/3 Attempts) Please guess the random number between and including 1 - 10: \n"))
            if Userinput == randomNumber:
                print("Correct Answer, Gameover!")
                guessed = True
            elif i!=2 :
                print("Incorrect Answer, Please try Again!")
            elif i==2 :
                print("Gameover! \nThe Anser was: " + str(randomNumber))

# Call Number Guesser
randomNumberGuesser()   