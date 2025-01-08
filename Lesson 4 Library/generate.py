# import random

# coin = random.choice(["Heads","Tails","Heads","Tails","Heads","Tails","Heads","Tails","Heads","Tails","Heads","Tails","Heads","Tails","Heads","Tails","Heads","Tails","Heads","Tails"])
# print(coin)

# from random import choice

# coin = choice(["Heads","Tails"])
# print(coin)

# from random import randint

# num = randint(1,99)
# print(num)

import random
cards = [ 'Jack', 'Queen', 'King', 'Ace']
random.shuffle(cards)
print(cards)
for card in cards:
    print(card)