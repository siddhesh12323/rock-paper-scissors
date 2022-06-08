import random


def game():
    users_choice = input("Rock, paper or scissors?: ").lower()
    available_choices = ["rock", "paper", "scissors"]
    computers_choice = random.choice(available_choices)
    if users_choice not in available_choices:
        print("Please enter valid entry!")
        game()
    else:
        if computers_choice == "rock":
            if users_choice == "rock":
                print("Your choice:", users_choice)
                print("Computer's choice:", computers_choice)
                print("It's a tie!")
                again_play()
            if users_choice == "paper":
                print("Your choice:", users_choice)
                print("Computer's choice:", computers_choice)
                print("You Win!")
                again_play()
            if users_choice == "scissors":
                print("Your choice:", users_choice)
                print("Computer's choice:", computers_choice)
                print("You Lose!")
                again_play()
        if computers_choice == "paper":
            if users_choice == "rock":
                print("Your choice:", users_choice)
                print("Computer's choice:", computers_choice)
                print("You Lose!")
                again_play()
            if users_choice == "paper":
                print("Your choice:", users_choice)
                print("Computer's choice:", computers_choice)
                print("It's a tie!")
                again_play()
            if users_choice == "scissors":
                print("Your choice:", users_choice)
                print("Computer's choice:", computers_choice)
                print("You Win!")
                again_play()
        if computers_choice == "scissors":
            if users_choice == "rock":
                print("Your choice:", users_choice)
                print("Computer's choice:", computers_choice)
                print("You Win!")
                again_play()
            if users_choice == "paper":
                print("Your choice:", users_choice)
                print("Computer's choice:", computers_choice)
                print("You Lose!")
                again_play()
            if users_choice == "scissors":
                print("Your choice:", users_choice)
                print("Computer's choice:", computers_choice)
                print("It's a tie!")
                again_play()


def again_play():

    play_again = input("Play again? y/n: ").lower()
    if play_again == "y":
        game()
    elif play_again == "n":
        print("Thanks for playing")
    else:
        print("Please enter y/n only!")
        again_play()


game()

