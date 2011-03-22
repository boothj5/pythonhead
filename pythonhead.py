suits = ["hearts", "spades", "diamonds", "clubs"]
ranks = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]

deck = [(x,y) for y in suits for x in ranks]

print deck
