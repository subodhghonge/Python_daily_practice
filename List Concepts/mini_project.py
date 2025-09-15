#.1. Student Score Tracker

# Concepts Used: list storage, sum(), max(), min(), loops, len().

# Problem Statement:

# Store marks of students in a list.

# Find average, highest, lowest, and display all scores.

def student_score_tracker():

    for i in range(n):
        score = int(input(f"Enter the number of students {i+1}: "))
        scores.append(score)

scores = []

n = int(input("Enter the number of students: "))
student_score_tracker()

while True:
    print(""" 
    1. Scores of all students
    2. Highest Score
    3. Average Score
    4. Lowerst Score
    5. Exit""")

    ch = int(input('Enter your choice(1-5): '))

    if ch == 1:
        print("Scores of all students:", scores)
    elif ch == 2:
        if scores:
            print("Highest Score:", max(scores))
        else:
            print("No scores available.")
    elif ch == 3:
        if scores:
            print("Average Score:", sum(scores) / len(scores))
        else:
            print("No scores available.")
    elif ch == 4:
        if scores:
            print("Lowest Score:", min(scores))
        else:
            print("No scores available.")
    elif ch == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")