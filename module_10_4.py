from threading import Thread
import gueue
from time import sleep
import random


class Table:

    def __init__(self, number):
        self.number = number
        self.guest  = None

class Cafe(gueue):

    def __init__(self, queue):
        self.queue = queue
        self.tables = ()

    def guest_arrival(self, *guests):   #(прибытие гостей)
        for guest in guests:
             while True:
                 self.tables = self.queue.put(guest)

    def discuss_guests(self, *guests):   # обслужить гостей
        guest =











        self.guests = guests





