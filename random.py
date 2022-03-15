from random import *

# Roll a dice
print(randint(1, 6))

# Flip a coin
coin = ["heads", "tails"]
print(choice(coin))

# Paper Cissors Rock
hand = ["paper", "cissors", "rock"]
print(choice(hand))

# burger making 
bun = ["toast", "bread"]
topping = ["tomato", "salad"]
cheese = ["tasty", "edam"]
patty = ["steak", "sausage"]
print("Sandwich:", choice(bun), choice(topping), choice(cheese), choice(patty))
