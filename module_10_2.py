import threading
import time


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

        def run(self):
        print(f'{self.name}, на нас напали!!!')
        count_day = 1
        count_warriors = 100 - self.power
        while count_warriors > 0:
            print(f'{self.name} сражается {count_day} день(дня), осталось {count_warriors} воинов \n{self.name}'
                  f' одержал победу {count_day} спустя')
            count_day += 1
            count_warriors -= self.power
            time.sleep(1)
        if count_warriors < 0:
            print(f'{self.name} сражается {count_day} день(дня), осталось 0 воинов')
        else:
            print(f'{self.name} сражается {count_day} день(дня), осталось {count_warriors} воинов')



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()


print('Все битвы закончились!')
