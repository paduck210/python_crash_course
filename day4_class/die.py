from random import randint

class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self, number):
        start = 0
        while number >= start:
            print(randint(1, self.sides))
            start += 1

ten_dice = Die(10)
ten_dice.roll_dice(10)

twnty_dice = Die(20)
twnty_dice.roll_dice(5)