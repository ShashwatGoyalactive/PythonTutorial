import random

class Dice:

    def roll(self):
        # x = random.randrange(6)+1
        # y = random.randrange(6) + 1
        x = random.randint(1,6)
        y =random.randint(1,6)
        return x,y


dice = Dice()
print(dice.roll())