import threading
import random
from time import sleep
from queue import Queue

class Table:    #столы

    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):                      # гость
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        sleep(random.randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = list(tables)
    def guest_arrival(self, *guests):     # прибытие гостей
        for guest in guests:
            table = self.find_free_table()
            if table:
                table.guest = guest
                guest.start()
                print(f'{guest.name} сел(-а) за стол номер {table.number}')
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')
    def discuss_guests(self):          # обслужить гостей
        while not self.queue.empty() or self.any_guest_still_seated():
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    next_guest = self.queue.get()
                    table.guest = next_guest
                    next_guest.start()
                    print(f'{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
    def find_free_table(self):
        for table in self.tables:
            if table.guest is None:
                return table
        return None
    def any_guest_still_seated(self):
        return any(table.guest is not None for table in self.tables)

tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()