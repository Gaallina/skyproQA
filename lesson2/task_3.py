import math


def square(side):
    if not isinstance(side, int):
        side = math.ceil(side)

    area = side * side
    return area


side_string = input("Enter the side length of a square: ")
side_length = float(side_string)
result = square(side_length)
print(f"The area of a square with the side of {side_length} equals {result}")
