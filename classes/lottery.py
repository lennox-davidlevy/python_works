from random import randint
from time import time


class Lotto:
    def __init__(self, numbers=6, numbers_range=49):
        self.history = []
        self.numbers = numbers
        self.numbers_range = numbers_range
        self.winning_lotto = self.create_play()
        self.number_of_tries = 0

    def create_play(self):
        temp_play = set()
        while len(temp_play) < self.numbers:
            temp_play.add(randint(1, self.numbers_range))
        return sorted(temp_play)

    def get_winning_lotto(self):
        print(f"Winning lotto numbers: {self.winning_lotto}")
        return self.winning_lotto

    def attempt_to_win(self):
        active_flag = True
        start = time()
        while active_flag:
            temp_play = self.create_play()
            self.number_of_tries += 1
            if temp_play == self.winning_lotto:
                time_elapsed = round(time() - start)
                active_flag = False
                print(
                    f"It took {self.number_of_tries} and {time_elapsed} seconds to win!"
                )
        return {
            "winning_lotto": self.winning_lotto,
            "winning_play": temp_play,
            "number_of_tries": self.number_of_tries,
            "time_elapsed": time_elapsed,
        }


new_lotto = Lotto()
new_lotto.get_winning_lotto()
print(new_lotto.attempt_to_win())
