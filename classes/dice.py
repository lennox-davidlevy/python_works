from random import choice, randint


class Dice:
    def __init__(self, number_of_dice=1, number_of_sides=6):
        self.rolls_history = []
        self.number_of_dice = number_of_dice
        self.number_of_sides = number_of_sides

    def roll_dice_individual_value_randint(self):
        temp_rolls = []
        for i in range(0, self.number_of_dice):
            temp_rolls.append(randint(1, self.number_of_sides))
        self.rolls_history.append(temp_rolls)
        return temp_rolls

    def roll_dice(self):
        dice_roll = self.roll_dice_individual_value_randint()
        dice_roll_sum = sum(dice_roll)
        return {"individual_dice_roll": dice_roll, "sum_of_dice": dice_roll_sum}

    def show_roll_history(self):
        if len(self.rolls_history) == 0:
            print(f"no history available")
            return False
        print(f"Last {len(self.rolls_history)} rolls:")
        for idx, roll in enumerate(self.rolls_history):
            print(f"\t{idx + 1}: {roll}")
        return self.rolls_history


# new_game = Dice(10, 10)
# for i in range(0, 11):
#    print(new_game.roll_dice())
# new_game.show_roll_history()
twenty_sided_game = Dice(number_of_sides=20)
for i in range(0, 11):
    print(twenty_sided_game.roll_dice())
twenty_sided_game.show_roll_history()
