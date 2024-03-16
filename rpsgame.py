import random


def win(userInput, cpInput):
    if userInput == "rock" and cpInput == "scissors":
        print("You Win!")
        return "U"
    elif userInput == "rock" and cpInput == "paper":
        print("You Lose!")
        return "C"
    elif userInput == "paper" and cpInput == "rock":
        print("You Win!")
        return "U"
    elif userInput == "paper" and cpInput == "scissors":
        print("You Lose!")
        return "C"
    elif userInput == "scissors" and cpInput == "paper":
        print("You Win!")
        return "U"
    elif userInput == "scissors" and cpInput == "rock":
        print("You Lose")
        return "C"
    else:
        print("Draw!!")
        return "D"


playerPoints = 0
computerPoints = 0
draw = 0

print("\n")
print("===========WELCOME TO ROCK-PAPER-SCISSORS GAME===========")
name = input("Please enter your name: ")

while True:

    choices = ["rock", "paper", "scissors"]
    print("-------------------------------------")
    print("Choose from: rock, paper, scissors")
    userInput = input("Enter your choice: ").lower()
    if userInput not in choices:
        print("-------------------------------------")
        print("Enter a valid choice")
        print("-------------------------------------")
        continue

    compInput = random.choice(choices)
    print("-------------------------------------")
    print(f"{name} choice: {userInput}")
    print(f"Computer Chose: {compInput}")
    print("-------------------------------------")
    result = win(userInput, compInput)

    if result == "U":
        playerPoints += 1
    elif result == "C":
        computerPoints += 1
    else:
        draw += 1

    print("-------------------------------------")
    print(f"{name} Points: {playerPoints}")
    print(f"Computer Points: {computerPoints}")
    print(f"Draws: {draw}")
    print("-------------------------------------")

    input2 = input("Do you want to play again? (Y/N)")
    if input2 != "y" and input2 != "Y":
        break

print("Goodbye :)")
