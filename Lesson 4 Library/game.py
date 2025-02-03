import random
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass
random_num =random.randint(1,level)
while True:
    try:
        guess_num = int(input("Guess: "))
        if guess_num <= 0:  # Ensure guess is positive
            continue
    except ValueError:
        continue  # Ignore non-numeric input
    if guess_num > random_num:
        print("Too large!")
    elif guess_num < random_num:
        print("Too small!")
    else:
        print("Just right!")
        break