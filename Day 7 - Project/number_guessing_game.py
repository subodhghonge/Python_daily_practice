num_to_guessed = 5

print("Welcome to the Number Guessing Game!")

while True:
    guess = int(input("Guess a number between 1 - 10: "))

    if guess > 10:
        print("Invalid input! You entered a number greater than 10. Exiting the game.")
        break

    if guess < num_to_guessed:
        print("Too Low!!, Try again:")
    elif guess == num_to_guessed:
        print(guess, "Congratulations! You guessed the correct number")
        break
    else:
        print("Too high!!, Try again:")