class Passenger(object):
    def __init__(self, aisle_movement_rate, seat_movement_rate, luggage_stowwing_rate, destination):
        self.aisle_movement_rate = aisle_movement_rate
        self.seat_movement_rate = seat_movement_rate
        self.luggage_stowwing_rate = luggage_stowwing_rate
        self.row, self.seat = destination

        self.time = 0

    def __repr__(self):
        return "Passenger seated @ ({0}, {1})".format(self.row, self.seat)

    def compute_time(self, row, seat):
        return self.aisle_movement_rate * row + self.seat_movement_rate * seat + abs(self.luggage_stowwing_rate)
