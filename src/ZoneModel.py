from src.Airplane import Airplane
from src.Passenger import Passenger

AISLE_MOVEMENT_RATE = 1
SEAT_MOVEMENT_RATE = 1
LUGGAGE_STOWWING_RATE = 1


class ZoneModel(object):
    def generate_zone(self, row, seats):
        group = []
        for seat in range(-1, -seats - 1, -1):
            group.append(Passenger(AISLE_MOVEMENT_RATE, SEAT_MOVEMENT_RATE, LUGGAGE_STOWWING_RATE, (row, seat)))
        for seat in range(1, seats + 1):
            group.append(Passenger(AISLE_MOVEMENT_RATE, SEAT_MOVEMENT_RATE, LUGGAGE_STOWWING_RATE, (row, seat)))
        return group

    def generate_zone_queue(self, rows, seats):
        queue = []
        for r in range(rows):
            queue.append(self.generate_zone(r, seats))
        return queue

    def generate(self, rows=3, seats=3):
        passenger_queue = self.generate_zone_queue(rows, seats)
        plane = Airplane(rows)
        plane.queue = passenger_queue
        return plane
