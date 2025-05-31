'''
1 for stone
0 for paper
-1 for scissors
'''
import random

status = {1: "stone", 0: "paper", -1: "scissors"}   

computer = random.choice([1, 0, -1])
user_input = input("Enter your choice (stone/paper/scissors): ").strip().lower()

if user_input == "stone":
    user = 1
elif user_input == "paper":
    user = 0
elif user_input == "scissors":
    user = -1
else:
    print("Invalid input! Please enter stone, paper, or scissors.")
    exit()


if user == computer:
    print("It's a draw!")

elif (user == 0 and computer == 1) or (user == -1 and computer == 0) or (user == 1 and computer == -1):
    print("You win!")

else:
    print("You Lose!")

print(f"Computer chose: {status[computer]}")
print(f"You chose: {status[user]}")
print("Game Over!")