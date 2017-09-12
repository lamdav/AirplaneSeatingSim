from graphics import *
import math
import time

class Visualizer(object):
    def __init__(self, plane):
        self.AirPlane = plane
        self.SeatWidth = 30
        self.Aisle = 10
        self.SEAT_ARRAY = None
        self.window = None
        self.PassengerSet = set()
        self.PERSON_SIZE = 7.5
        self.OBJECT_ARRAY = []
        self.Label = None

    def build(self):
        window = GraphWin("Simulator", 800, 400)
        self.Label = Text(Point(5, 5), "Time Units: 0").setSize(18)
        pl = self.AirPlane.plane
        x = 50
        y = 50
        SeatWidth = 30
        AllSeat = []

        for k in range(math.ceil(len(pl) / 5)):
            CurrentRow = pl[k]
            tempArr = []
            for j in range(len(CurrentRow)):
                newX = x + k * SeatWidth / 2 * 2
                newY = y + j * SeatWidth / 2 * 2
                newP = Point(newX, newY)
                cir = Circle(newP, SeatWidth / 2)
                if (pl[k][j] != 'A'):
                    tempArr.append(cir)
                    window.addItem(cir)
                else:
                    p1 = cir.getP1()
                    p2 = cir.getP2()
                    rec = Rectangle(p1, p2)
                    window.addItem(rec)
                    tempArr.append(rec)
            AllSeat.append(tempArr)
            window.redraw
        self.SEAT_ARRAY = AllSeat
        self.window = window
        window.redraw()

    def run(self):
        window = self.window
        currentPlaneState = self.AirPlane.plane
        for obj in self.OBJECT_ARRAY:
            print("undraw")
            obj.undraw()

        AllDrawn = []
        window.redraw()

        for k in range(math.ceil(len(currentPlaneState))):
            SubRow = currentPlaneState[k]
            for j in range(len(SubRow)):
                if (SubRow[j] != 0 and SubRow[j] != 'A'):
                    print(SubRow, k, j)
                    temp = math.floor(k / 5)
                    print(temp, j)
                    obj = self.SEAT_ARRAY[temp][j]
                    P = obj.getCenter()
                    x = P.getX()
                    y = P.getY()
                    if (j == 3):
                        x += (j - 2) * (self.SeatWidth / 4)
                    cir = Circle(Point(x, y), self.PERSON_SIZE)
                    cir.setFill("red")
                    cir.draw(window)
                    AllDrawn.append(cir)
        self.OBJECT_ARRAY = AllDrawn
        window.redraw()
        time.sleep(1)
