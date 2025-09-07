import math


def shapee():
    print("1) Triangle")
    print("2) Rectangle")
    print("3) Square")
    print("4) circle")
    print("5) Quit")
    shape = int(input("Which shape: "))
    if shape == 1:
        triangle()
    elif shape == 2:
        rectangle()
    elif shape == 3:
        square()
    elif shape == 4:
        circle()
    else:
        print('Quit')


def triangle():
    height = int(input("height:"))
    base = int(input("base:"))
    print(f"The area is {(base * height) / 2}")


def rectangle():
    lenght = int(input("lenght: "))
    width = int(input("width: "))
    print(f"The are is {lenght * width}")


def square():
    side = int(input("side: "))
    print(f"The area is {side * side}")


def circle():
    radius = int(input("radius: "))
    print(f"The are is{(radius ** 2) * math.pi}")





def main():
    print("==================")
    print("Area Calculator")
    print("==================")
    shapee()

main()