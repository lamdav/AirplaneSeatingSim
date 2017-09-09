class Airplane(object):
    def __init__(self, rows):
        ROW_COMPONENT = [0, 0, 0, 'A', 0, 0, 0]
        self.SEAT_SIZE = 3
        self.plane = [ROW_COMPONENT for _ in range(self.SEAT_SIZE * rows)]
        self.passengers = []

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

    def load_passengers(passengers):
        self.passengers = passengers
