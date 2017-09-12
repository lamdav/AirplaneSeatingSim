import random
random.seed(123)

from Passenger import Passenger
from Airplane import Airplane
from Visualizer import *

AISLE_MOVEMENT_RATE = 1
SEAT_MOVEMENT_RATE = 1
LUGGAGE_STOWWING_RATE = 1

# Not used. Generates all possible passengers.
def generate_passengers(rows, seats):
    passengers = []
    for row in range(rows):
        for seat in range(-seats, seats + 1 ):
            passengers.append(Passenger(AISLE_MOVEMENT_RATE, SEAT_MOVEMENT_RATE, LUGGAGE_STOWWING_RATE, (row, seat)))

    return passengers

def make_alternating_group(rows, start):
    group = []
    for row in range(rows):
        group.append(Passenger(AISLE_MOVEMENT_RATE, SEAT_MOVEMENT_RATE, LUGGAGE_STOWWING_RATE, (row, start)))
        start = -start
    return group

def generate_queue(rows, seats):
    queue = []
    for seat in range(seats, 0, -1):
        queue.append(make_alternating_group(rows, seat))
        queue.append(make_alternating_group(rows, -seat))
    return queue

def main():
    rows = 3
    seats = 3

    passenger_queue = generate_queue(rows, seats)
    plane = Airplane(rows)

    plane.set_queue(passenger_queue)

    vis = Visualizer(plane)
    vis.build()

    for step, time_steps in plane.step():
        print("Time Units take: {0}".format(time_steps))
        vis.run()
        print(step)


if __name__ == '__main__':
    main()
