from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = str(name)
        self.power = int(power)

    def run(self):
        print(f"{self.name}, на нас напали!")
        enemy = 100
        for i in range(enemy):
            enemy -= self.power
            print(f'{self.name} сражается {i + 1} дней..., осталось {enemy} воинов.\n')
            if enemy == 0:
                print(f'{self.name} одержал победу спустя {i + 1} дней(дня)!')
                break


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
