import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.Airplane import Airplane
from src.Passenger import Passenger
from src.Visualizer import Visualizer

AISLE_MOVEMENT_RATE = 1
SEAT_MOVEMENT_RATE = 1
LUGGAGE_STOWWING_RATE = 1

def make_alternating_group(rows, seat):
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

def generate_queue(rows, seats):
    """
        Create the list of list of Passengers (queue) where each inner list are Passenegers seated
        in alternating rows.

        :param rows: Positive Integer of rows
        :param seats: Positive Integer of seats on each side of a row
        :return: List of list of Passengers
    """
    queue = []
    for seat in range(seats, 0, -1):
        queue.append(make_alternating_group(rows, seat))
        queue.append(make_alternating_group(rows, -seat))

    queue.reverse()
    return queue

def generate_zone(row, seats):
    group = []
    for seat in range(-1, -seats - 1, -1):
        group.append(Passenger(AISLE_MOVEMENT_RATE, SEAT_MOVEMENT_RATE, LUGGAGE_STOWWING_RATE, (row, seat)))
    for seat in range(1, seats + 1):
        group.append(Passenger(AISLE_MOVEMENT_RATE, SEAT_MOVEMENT_RATE, LUGGAGE_STOWWING_RATE, (row, seat)))
    return group

def generate_zone_queue(rows, seats):
    queue = []
    for r in range(rows):
        queue.append(generate_zone(r, seats))
    return queue

def main():
    rows = 50
    seats = 3

    # passenger_queue = generate_queue(rows, seats)
    passenger_queue = generate_zone_queue(rows, seats)
    plane = Airplane(rows)

    plane.queue = passenger_queue

    vis = Visualizer(plane)
    vis.build()

    for step, time_steps in plane.step():
        print("Time Units take: {0}".format(time_steps))
        vis.run()
        print(step)


if __name__ == '__main__':
    main()
