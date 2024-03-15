import random


def get_choices():
    user_choice = input("Enter your choice (rock, scissors, paper): ")

    choice = ["rock", "scissors", "paper"]
    computer_choise = random.choice(choice)

    choices = {"player": user_choice, "computer": computer_choise}
    return choices


def check_win(player, computer):
    print(f"You chose:  {player}, computer chose:  {computer}")
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cuts paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cuts paper! You win!"
        else:
            return "Rock smashes scissors! You lose."


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)