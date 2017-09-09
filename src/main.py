import random
random.seed(123)
class Passenger():
    def __init__(self,x,y,age):
        self.row = x
        self.col = 0
        if(y>=3):
            self.col = y-3
        else:
            self.col = abs(y-2)
        self.time = 0
        self.age = age
    def computeTime(self):
        self.time = timeFunction(self.row,self.col)
def timeFunction(x,y):
    """
    T(x,y) =  Ax+By + C
    0 1 2 | | 3 4 5
    :param x: row
    :param y: column
    :return: int: T
    """
    A = 3
    B = 10
    C = 6
    return A*x+B*y+C

def main():
    R = 10 #rows in plane
    Manifest = []
    for k in range(1,R+1):
        row =  []
        for j in range(6):
            age = random.randint
            p = Passenger(k,j,age)
            p.computeTime()
            row.append(p)
        Manifest.append(row)




if __name__ == '__main__':
    main()
