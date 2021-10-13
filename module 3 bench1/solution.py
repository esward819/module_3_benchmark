from typing import List
class DogBoarder:
    count = 0
    def __init__(self, total_slots, daily_rate):
        self.total_slots = total_slots
        self.daily_rate = daily_rate
        self.dogs = []
        self.picks = []
    def slots_occupied(self):
        return self.count
    def board(self, dog_num, dog_breed, owner_num):
        if self.total_slots != self.count:
            self.bigger_dogs = [dog_num, dog_breed, owner_num]
            self.count += 1
            self.dogs.append(self.bigger_dogs)
        else:
            raise ValueError
    def is_full(self):
        if self.total_slots == self.count:
            return True
        return False
    def pick_up(self, dog, breed, owner, price):
        self.bigger_picks = [dog, breed, owner]
        if self.bigger_picks in self.dogs:
            self.dogs.remove(self.bigger_picks)
            self.price = self.daily_rate * price
            self.count -= 1
            return self.price
        else:
            raise ValueError