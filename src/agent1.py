import random

def main():


    AgentBuilder()


    """ Calls the   TEST   functions in this module. """


#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
def AgentBuilder():
    A = 0
    B = 0
    C = 0
    R = random.randint(1, 15)
    age = random.randint(1, 100)
    anx = random.randint(1, 25)
    drunk = random.randint(1, 100)
    op = random.randint(1, 10)
    fat = random.randint(1, 100)
# recurring flyer creates a baseline of 25 or 10
    if R == 1:
        A = 25
        B = 25
        C = 25
    else:
        A = 10
        B = 10
        C = 10
# older man adds 5 to 13 units
    if age >= 85:
        A += (age - 75) / 2
        B += (age - 75) / 2
        C += (age - 75) / 2
# student subtracts 2 to 5 units
    elif age < 25:
        A += -((25 - age) / 8 + 2)
        B += -((25 - age) / 8 + 2)
        C += -((25 - age) / 8 + 2)
# child adds 4 to 9 units
    elif age >= 25 and age < 35:
        A += ((35 - age) * 6) / 10 + 3
        B += ((35 - age) * 6) / 10 + 3
        C += ((35 - age) * 6) / 10 + 3
# anxious flyers
    if anx <= 2:
        A += 5
        B += 5
        C += 5
# overpacked flyers
    if op == 1:
        A += 5
        B += 5
        C += 5
# drunk flyers
    if drunk == 1 and age >= 35:
        A += 10
        B += 10
        C += 10
# fat people
    if fat == 1 and age < 25 or age > 35:
        A += 7
        B += 7
        C += 7

    print(A)
    print(B)
    print(C)
    print(R)
    print(age)
    print(anx)
    print(drunk)
    print(op)
    print(fat)

if __name__ == '__main__':
    main()
