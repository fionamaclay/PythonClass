import random

def add_scores():
    score = random.randint(0, 100)

    with open("scores.txt", "a") as fh:
        fh.write(f"{score}\n")

def last_score():
    with open("scores.txt", "r") as fh:
        for score in fh.readlines():
            continue
    
    print(f"Your last score was: {score}", end="")

add_scores()
last_score()