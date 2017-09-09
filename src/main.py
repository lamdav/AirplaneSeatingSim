import random
random.seed(123)

from Passenger import Passenger
from Airplane import Airplane

AISLE_MOVEMENT_RATE = 1
SEAT_MOVEMENT_RATE = 1
LUGGAGE_STOWWING_RATE = 1

def generate_passengers(rows, seats):
    passengers = []
    for row in range(rows):
        for seat in range(-seats, seats + 1 ):
            passengers.append(Passenger(AISLE_MOVEMENT_RATE, SEAT_MOVEMENT_RATE, LUGGAGE_STOWWING_RATE, (row, seat)))

    return passengers

def main():
    rows = 10
    seats = 3

    passengers = generate_passengers(rows, seats)
    plane = Airplane(rows)

    plane.load_passengers(passengers)


if __name__ == '__main__':
    main()
