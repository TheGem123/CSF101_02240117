
# Part_A-  Number-Guessing-Game

import random

""" Randomly select a number within the range defined by lower_value and upper_value"""


def number_guessing_game():
    lowest_value = 1
    highest_value = 90

    confidential_number = random.randint(lowest_value, highest_value)
    guesses = 0
    is_running = True
    print("Python Number Guessing Game")  # welcome message
    # Prompt the user
    print(f"Select a number between {lowest_value} and {highest_value}")

    while is_running:

        guess = input("Enter your guess: ")
        if guess.isdigit():
            guess = int(guess)
            guesses += 1
            if guess < lowest_value or guess > highest_value:
                print("That number is out of range")
            elif guess < confidential_number:
                print("Too low!, Try better!")
            elif guess > confidential_number:
                print("Too high! Try better!")
            else:
                print(
                    f"CORRECT! The confidential_number was {confidential_number}")
                print(f" Number of guesses")
                is_running = True
        else:
            print("Invalid guess")
            print(
                f"Please select a number between {lowest_value} and {highest_value}")


# Part_B- Rock-Paper-Scissor
import random

def rock_paper_scissors_game():

    options = ("rock", "paper", "scissors")
    playing = True

    while playing:

        player = None
    # Using choice method to allow computer to pick a random options.
        computer = random.choice(options)

    while player not in options:  # Allowing the player to pick the valid option
        player = input("Enter a choice(rock,paper,scissors): ")

    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("Its a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")


while True:
    print("""Select your function from 1-3:
          1.Guess number game
          2.Rock paper scissor game
          3.Exit programe""")
    option = int(input("Enter your choice:"))

    if option == 1:
        number_guessing_game()

    elif option == 2:
        rock_paper_scissors_game()

    elif option == 3:
        print("THANK YOU FOR YOUR TIME!")
        break
    else:
        print("Invalid choice!")
