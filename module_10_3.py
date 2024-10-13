import random
from time import sleep
import threading
from threading import Lock
class Bank:

    def __init__(self):
        super().__init__()
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            random_number_up = random.randint(50, 500)
            self.balance += random_number_up
            print(f"Пополнение: {random_number_up}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for i in range(100):
            random_balance_reduction = random.randint(50, 500)
            print(f"Запрос на {random_balance_reduction}")
            if random_balance_reduction <= self.balance:
                self.balance -= random_balance_reduction
                print(f"Снятие: {random_balance_reduction}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
                sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')