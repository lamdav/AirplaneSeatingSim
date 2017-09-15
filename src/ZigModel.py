from src.Airplane import Airplane
from src.Passenger import Passenger

AISLE_MOVEMENT_RATE = 1
SEAT_MOVEMENT_RATE = 1
LUGGAGE_STOWWING_RATE = 1


class ZigModel(object):
    def make_alternating_group(self, rows, seat):
        """
            Returns a list of alternating Passengers.

            :param rows: Positive Integer of rows
            :param seats: Positive Integer of seats on each side of a row
            :return: List of Passengers
        """
        group = []
        for row in range(rows):
            group.append(Passenger(AISLE_MOVEMENT_RATE, SEAT_MOVEMENT_RATE, LUGGAGE_STOWWING_RATE, (row, seat)))
            seat = -seat
        return group

    def generate_queue(self, rows, seats):
        """
            Create the list of list of Passengers (queue) where each inner list are Passenegers seated
            in alternating rows.

            :param rows: Positive Integer of rows
            :param seats: Positive Integer of seats on each side of a row
            :return: List of list of Passengers
        """
        queue = []
        for seat in range(seats, 0, -1):
            queue.append(self.make_alternating_group(rows, seat))
            queue.append(self.make_alternating_group(rows, -seat))

        queue.reverse()
        return queue

    def generate(self, rows=3, seats=3):
        passenger_queue = self.generate_queue(rows, seats)
        plane = Airplane(rows)
        plane.queue = passenger_queue
        return plane
