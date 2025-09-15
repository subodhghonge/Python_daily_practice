# Lottery System

# 👉 Concepts Used: random.choice, list iteration, unique selection.

# Problem Statement:

# Store participants in a list.

# Randomly select winners.
import random

def lottery_system():
    participants = []

    n = int(input("Enter the number of participants : "))
    for i in range(n):
        name = input(f"Enter the name of participant {i+1}: ")
        participants.append(name)

    print(f'Participants - {participants}')

    winners_count = int(input("Enter the number of winners: "))

    if winners_count > len(participants):
        print("Not enough participants for winners!")
    else:
        winners = random.sample(participants, winners_count)
        print(f"Winners, {winners}")

lottery_system()