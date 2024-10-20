from time import sleep
from threading import Thread

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f'{self.name} на нас напали {self.enemies} врагов!')

        while self.enemies > 0:
            self.enemies -= self.power
            self.days += 1
            print(f'После {self.days}-ого дня сражения у {self.name} осталось {self.enemies} врагов')
            sleep(1)
        print(f'{self.name} победил за {self.days} дней!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()