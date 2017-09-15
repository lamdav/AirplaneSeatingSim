import math
import time

from tkinter import *

from src.graphics import *

class Visualizer(object):
    def __init__(self, plane):
        self.airplane = plane
        self.SEAT_WIDTH = 30

        self.PERSON_SIZE = 7.5

        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 400
        self.window = GraphWin("Plane Seating Simulator", self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

        self.label = Text(Point(self.WINDOW_WIDTH / 2, self.WINDOW_HEIGHT / 25), "Time Units: 0")
        self.label.setSize(20)

        self.window.addItem(self.label)

        self.internal_plane = []
        self.passengers = []
        self.at_assigned_seat = set()
        self.PASSENGER_COLORS = ["red", "blue"]

    def draw_plane(self, plane_state):
        INITIAL_POSITION = 50
        x = INITIAL_POSITION
        y = INITIAL_POSITION

        for row_index in range(int(math.ceil(len(plane_state) / self.airplane.SEAT_SIZE))):
            row_components = []
            current_row = plane_state[row_index]
            for seat_index in range(len(current_row)):
                position = current_row[seat_index]

                y += self.SEAT_WIDTH
                center = Point(x, y)

                item = Circle(center, self.SEAT_WIDTH / 2)
                if (position != self.airplane.EMPTY_SEAT):
                    item = Rectangle(item.getP1(), item.getP2())

                self.window.addItem(item)
                row_components.append(item)

            self.internal_plane.append(row_components)
            x += self.SEAT_WIDTH
            y = INITIAL_POSITION

        self.window.redraw()

    def undraw_passengers(self):
        for passenger in self.passengers:
            passenger.undraw()
        self.passengers = []

    def draw_state(self, plane_state):
        # Remove all moving passengers.
        self.undraw_passengers()

        color = 0
        for row in range(len(plane_state)):
            for seat in range(len(plane_state[row])):
                if (self.airplane.is_passenger(plane_state[row][seat])):
                    passenger = plane_state[row][seat]
                    if (passenger in self.at_assigned_seat):
                        continue

                    real_row, real_seat = self.airplane.convert_internal_to_real_position(row, seat)

                    adjusted_real_row = int(math.floor(real_row))
                    adjusted_real_seat = int(math.floor(real_seat)) + self.airplane.AISLE

                    item = self.internal_plane[adjusted_real_row][adjusted_real_seat]
                    passenger_item = Circle(item.getCenter(), self.PERSON_SIZE)
                    passenger_item.setFill(self.PASSENGER_COLORS[color % len(self.PASSENGER_COLORS)])
                    color += 1

                    passenger_item.draw(self.window)

                    if (passenger.is_at_assigned_seat(real_row, real_seat)):
                        self.at_assigned_seat.add(passenger)
                    else:
                        self.passengers.append(passenger_item)



    def update_time_step(self, time_step):
        self.label.setText("Time Step: {0}".format(time_step))

    def run(self):
        self.draw_plane(self.airplane.plane)
        for plane_state, time_step in self.airplane.step():
            self.draw_state(plane_state.plane)
            self.update_time_step(time_step)
