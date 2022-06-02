
import random

choices = ["r","p","s"]

computer = random.choice(choices)
player = None

player = input("R (rock), P (paper), or S (scissors)?: ").lower()

while True:
    if player == computer:
        print("It's a Tie!")
        computer = random.choice(choices)
        player = input("R (rock), P (paper), or S (scissors)?: ").lower()
    if player != computer:
        break

while player not in choices:
    print("Not an option: Pick either R, P or S")
    player = input("R (rock), P (paper), or S (scissors)?: ").lower()

if player == "r":
    if computer == "p":
        print(f"Player(rock) : CPU(paper)")
        print("You lose!")
    if computer == "s":
        print(f"Player(rock) : CPU(scissors)")
        print("You win!")
elif player == "s":
    if computer == "p":
        print(f"Player(scissors) : CPU(paper)")
        print("You win!")
    if computer == "r":
        print(f"Player(scissors) : CPU(rock)")
        print("You lose!")
elif player == "p":
    if computer == "r":
        print(f"Player(paper) : CPU(rock)")
        print("You win!")
    if computer == "s":
        print(f"Player(paper) : CPU(scissors)")
        print("You lose!")
