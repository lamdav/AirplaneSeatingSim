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

    def set_queue(self, queue):
        self.queue = queue

    def queue_is_empty(self):
        return len(self.queue) == 0

    def queue_get_next(self):
        return self.queue.pop(0)

    def can_load_passenger(self):
        """
            Returns True if the Airplane can load a new passenger.

            This is done by checking if any passenger is in the first row.
        """
        for row in range(self.SEAT_SIZE):
            if (self.plane[row][self.AISLE] != self.AISLE_INDICATOR):
                return False
        return True

    def load_passenger(self, passengers):
        self.plane[0][self.AISLE] = passengers
        return (0, self.AISLE)

    def convert_internal_to_real_position(self, internal_row, internal_seat):
        """
            Returns the Passenger (Real) coordinate position.

            :param internal_row:
            :param internal_seat:
            :return:
        """
        real_row = (internal_row + 1) / self.SEAT_SIZE
        real_seat = internal_seat - self.SEAT_PER_SIDE_PER_ROW
        return (real_row, real_seat)

    def convert_real_to_internal_position(self, real_row, real_seat):
        internal_row = int(real_row * self.SEAT_SIZE - 1)
        internal_seat = real_seat + self.SEAT_PER_SIDE_PER_ROW
        return (internal_row, internal_seat)

    def move_passengers(self, loaded_passengers):
        # Move the passenger farthest down the plane before moving others.
        # loaded_passengers is an array (Passenger, current_position)
        movable_loaded_passengers = []
        for i in range(len(loaded_passengers)):
            passenger_data = loaded_passengers[i]
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

            internal_row, internal_seat = self.convert_real_to_internal_position(real_row, real_seat)

            self.plane[internal_row][internal_seat] = passenger
            if (not passenger.is_at_assigned_seat(real_row, real_seat)):
                movable_loaded_passengers.append((passenger, (internal_row, internal_seat)))

        return movable_loaded_passengers

    def step(self):
        while (not self.queue_is_empty()):
            passenger_line = self.queue_get_next()

            passenger_index = 0
            loaded_passengers = []
            while (passenger_index < len(passenger_line)):
                # Check if the first row is empty.
                # If so, load a passenger.
                if (self.can_load_passenger()):
                    loaded_position = self.load_passenger(passenger_line[passenger_index])
                    loaded_passengers.append((passenger_line[passenger_index], loaded_position))
                    passenger_index += 1

                # Move all passengers that are currently loaded.
                loaded_passengers = self.move_passengers(loaded_passengers)
                # yield self

            while (len(loaded_passengers) != 0):
                loaded_passengers = self.move_passengers(loaded_passengers)
                # yield self
