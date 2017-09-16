from random import randint

from src.Airplane import Airplane
from src.Passenger import Passenger

AISLE_MOVEMENT = 5
SEAT_MOVEMENT_RATE = 1
LUGGAGE_STOWWING_RATE = 1


class ZoneModel(object):
    def __init__(self, constant_movement):
        self.constant_movement = constant_movement

    def generate_zone(self, row, seats):
        """
            Generates a Zone (window, middle, aisle, window, middle, aisle) of Passenger for a given row and
            number of seats.

            :param row: Number
            :param seats: Number
            :return: List of Passenger
        """
        group = []
        for seat in range(-1, -seats - 1, -1):
            if (self.constant_movement):
                movement_rate = 1
            else:
                movement_rate = randint(1, 10) / AISLE_MOVEMENT
            group.append(Passenger(movement_rate, SEAT_MOVEMENT_RATE, LUGGAGE_STOWWING_RATE, (row, seat)))
        for seat in range(1, seats + 1):
            if (self.constant_movement):
                movement_rate = 1
            else:
                movement_rate = randint(1, 10) / AISLE_MOVEMENT
            group.append(Passenger(movement_rate, SEAT_MOVEMENT_RATE, LUGGAGE_STOWWING_RATE, (row, seat)))
        return group

    def generate_zone_queue(self, rows, seats):
        """
            Returns a queue (List of List) of Passengers.

            :param rows: Number
            :param seats: Number
            :return: List of List of Passengers
        """
        queue = []
        for r in range(rows):
            queue.append(self.generate_zone(r, seats))
        return queue

    def generate(self, rows=3, seats=3):
        """
           Returns an Airplane loaded with passengers.

           :param rows: Number
           :param seats: Number
           :return: Airplane
        """
        passenger_queue = self.generate_zone_queue(rows, seats)
        plane = Airplane(rows)
        plane.queue = passenger_queue
        return plane
