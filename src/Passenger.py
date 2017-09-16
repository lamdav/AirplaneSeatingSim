import math

from src.Airplane import Airplane


class Passenger(object):
    def __init__(self, aisle_movement_rate, seat_movement_rate, luggage_stowwing_rate, destination):
        self.row, self.seat = destination

        self.aisle_movement_rate = aisle_movement_rate
        self.seat_movement_rate = seat_movement_rate
        self.luggage_stowwing_rate = luggage_stowwing_rate

        self.time = 0

    def __repr__(self):
        return "Passenger seated @ ({0}, {1})".format(self.row, self.seat)

    def move(self, current_row, current_seat):
        """
            Returns the (row, seat) coordinate the Passenger is in.

            :param current_row: Number
            :param current_seat: Number
            :return: (new_row, new_number)
        """
        target_row = self.row + Airplane.SEAT_ENTRANCE_OFFSET
        if (current_row == target_row):
            if (current_seat == self.seat):
                return (current_row, current_seat)
            else:
                return (current_row, current_seat + (int(math.copysign(1, self.seat)) * self.seat_movement_rate))
        else:
            new_row = round(current_row + self.aisle_movement_rate, 2)  # Python will bug out with floats occasionally.
            if (new_row > target_row):
                new_row = target_row
            return (new_row, current_seat)

    def is_at_assigned_seat(self, real_row, real_seat):
        """
            Returns True if the given row and seat are the assigned seating.

            :param real_row: Number
            :param real_seat: Number
            :return: Boolean
        """
        target_row = self.row + Airplane.SEAT_ENTRANCE_OFFSET
        return (real_row == target_row and real_seat == self.seat)
