import random

options = ["rock", "paper", "scissors"]
user = input("Choose rock, paper, or scissors ")
computer = random.choice(options)

print("opponent chose", computer)

if user == computer:
    print("You tied")
elif user == "rock" and computer == "scissors":
    print("You won! rock beats scissors")
elif user == "paper" and computer == "rock":
    print("You won! paper beats rock")
elif user == "scissors" and computer == "paper":
    print("You won! scissors beats paper")
else:
    print('You lose!')