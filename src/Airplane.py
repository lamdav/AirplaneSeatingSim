class Airplane(object):
    SEAT_ENTRANCE_OFFSET = 0.6

    def __init__(self, rows):
        self.AISLE_INDICATOR = "A"
        self.EMPTY_SEAT = 0
        self.SEAT_SIZE = 5
        self.SEAT_PER_SIDE_PER_ROW = 3
        self.AISLE = 3

        self.plane = [[self.EMPTY_SEAT, self.EMPTY_SEAT, self.EMPTY_SEAT, self.AISLE_INDICATOR, self.EMPTY_SEAT, self.EMPTY_SEAT, self.EMPTY_SEAT] for _ in range(self.SEAT_SIZE * rows)]
        self.queue = []

    def __repr__(self):
        ROW_SEPARATOR = "------------------------\n"
        builder = ROW_SEPARATOR
        row = 0

        string_plane = list(map(str, self.plane))
        for component in string_plane:
            builder += "{0}\n".format(component)
            row += 1

            if (row % self.SEAT_SIZE == 0):
                builder += ROW_SEPARATOR

        return builder

    def queue_is_empty(self):
        """
            Returns True if the plane queue is empty.

            :return: Boolean
        """
        return len(self.queue) == 0

    def queue_get_next(self):
        """
            Returns the first Passenger of the queue.

            :return: Passenger
        """
        return self.queue.pop()

    def can_load_passenger(self):
        """
            Returns True if the Airplane can load a new passenger.

            This is done by checking if any passenger is in the first row.

            :return: Boolean
        """
        for row in range(self.SEAT_SIZE):
            if (self.plane[row][self.AISLE] != self.AISLE_INDICATOR):
                return False
        return True

    def load_passenger(self, passenger):
        """
            Loads a passenger in the front of the plane.

            :param passengers: Passenger
            :return: position of the loaded passenger (row, seat)
        """
        self.plane[0][self.AISLE] = passenger
        return (0, self.AISLE)

    def convert_internal_to_real_position(self, internal_row, internal_seat):
        """
            Returns the real position given an internal position.

            :param internal_row: Number
            :param internal_seat: Number
            :return: Real Coordinate (row, seat)
        """
        real_row = (internal_row + 1) / self.SEAT_SIZE
        real_seat = internal_seat - self.SEAT_PER_SIDE_PER_ROW
        return (real_row, real_seat)

    def convert_real_to_internal_position(self, real_row, real_seat):
        """
            Returns the internal position given a real position.

            :param real_row:  Number
            :param real_seat: Number
            :return: Internal Coordinate (row, seat)
        """
        internal_row = int(real_row * self.SEAT_SIZE - 1)
        internal_seat = real_seat + self.SEAT_PER_SIDE_PER_ROW
        return (internal_row, internal_seat)

    def is_conflict_in_path(self, old_position, new_position):
        """
            Returns True if there is another Passenger in the route from the old_position to the new_position.

            :param old_position: Internal Position (row, seat)
            :param new_position: Internal Position (row, seat)
            :return: Boolean
        """
        internal_row, internal_seat = old_position
        new_internal_row, new_internal_seat = new_position

        if (internal_row == new_internal_row):
            start, end = internal_seat, new_internal_seat
            vary_by_row = False
        else:
            start, end = internal_row, new_internal_row
            vary_by_row = True

        if (start > end):
            start, end = end, start

        for k in range(start, end + 1):
            if (vary_by_row):
                position = self.plane[k][internal_seat]
            else:
                position = self.plane[internal_row][k]
            if (position != self.EMPTY_SEAT and position != self.AISLE_INDICATOR):
                return True

        return False

    def move_passengers(self, loaded_passengers):
        """
            Moves all passengers in the load_passengers array.

            :param loaded_passengers: List of Passengers that loaded and can move
            :return: List of Passengers that are loaded but not at their assigned seating
        """
        # Move the passenger farthest down the plane before moving others.
        # loaded_passengers is an array (Passenger, current_position)
        movable_loaded_passengers = []
        for passenger_data in loaded_passengers:
            passenger, current_position = passenger_data

            internal_row, internal_seat = current_position
            real_row, real_seat = self.convert_internal_to_real_position(internal_row, internal_seat)

            # If the passenger is in the aisle, replace the passenger with the indicator.
            # Otherwise, set it to the empty seat indicator.
            if (internal_seat == self.AISLE):
                self.plane[internal_row][internal_seat] = self.AISLE_INDICATOR
            else:
                self.plane[internal_row][internal_seat] = self.EMPTY_SEAT

            real_row, real_seat = passenger.move(real_row, real_seat)
            new_internal_row, new_internal_seat = self.convert_real_to_internal_position(real_row, real_seat)

            # Check if there will be any hoping or landing on existing Passengers. If so, do not allow it.
            if (self.is_conflict_in_path((internal_row, internal_seat), (new_internal_row, new_internal_seat))):
                continue

            self.plane[new_internal_row][new_internal_seat] = passenger
            if (not passenger.is_at_assigned_seat(real_row, real_seat)):
                movable_loaded_passengers.append((passenger, (new_internal_row, new_internal_seat)))

        return movable_loaded_passengers

    def step(self):
        """
            Steps through the model and yields it at each completed time iteration.

            :return: yields (self, current time iteration)
        """
        time_steps = 0
        while (not self.queue_is_empty()):
            passenger_line = self.queue_get_next()

            loaded_passengers = []
            while (len(passenger_line) != 0):
                # Check if the first row is empty.
                # If so, load a passenger.
                if (self.can_load_passenger()):
                    passenger = passenger_line.pop()
                    loaded_position = self.load_passenger(passenger)
                    loaded_passengers.append((passenger, loaded_position))

                # Move all passengers that are currently loaded.
                loaded_passengers = self.move_passengers(loaded_passengers)
                time_steps += 1
                yield (self, time_steps)

            # All loaded passenger for a given line must be seated before loading another group.
            while (len(loaded_passengers) != 0):
                loaded_passengers = self.move_passengers(loaded_passengers)
                time_steps += 1
                yield (self, time_steps)

