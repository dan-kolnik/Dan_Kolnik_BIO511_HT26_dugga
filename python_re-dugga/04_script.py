# Q4

import random

# Task A

rps = ["rock", "paper", "scissors"]

Alice = random.choice(rps)
Bob = random.choice(rps)

print("Alice: " + Alice)
print("Bob: " + Bob)

if Alice == Bob:
    print("Draw")
elif Alice == "rock" and Bob == "scissors":
    print("Alice won this game")
elif Alice == "rock" and Bob == "paper":
    print("Bob won this game")
elif Alice == "paper" and Bob == "scissors":
    print("Bob won this game")
elif Alice == "paper" and Bob == "rock":
    print("Alice won this game")
elif Alice == "scissors" and Bob == "rock":
    print("Bob won this game")
elif Alice == "scissors" and Bob == "paper":
    print("Alice won this game")


# Task B

dict = {"alice": 0, "bob": 0, "draw": 0}

for game in range(20):
    Alice = random.choice(rps)
    Bob = random.choice(rps)

    if Alice == Bob:
        dict["draw"] += 1
    elif Alice == "rock" and Bob == "scissors":
        dict["alice"] += 1
    elif Alice == "rock" and Bob == "paper":
        dict["bob"] += 1
    elif Alice == "paper" and Bob == "scissors":
        dict["bob"] += 1
    elif Alice == "paper" and Bob == "rock":
        dict["alice"] += 1
    elif Alice == "scissors" and Bob == "rock":
        dict["bob"] += 1
    elif Alice == "scissors" and Bob == "paper":
        dict["alice"] += 1

print(dict)