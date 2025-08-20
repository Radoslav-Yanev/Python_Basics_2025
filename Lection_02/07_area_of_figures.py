from math import pi

figure = input()
area = 0.0

if figure == "square":
    square_side = float(input())
    area = square_side * square_side
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif figure == "circle":
    radius = float(input())
    area = pi * radius * radius
elif figure == "triangle":
    triangle_side = float(input())
    height = float(input())
    area = (triangle_side * height) / 2

print(f"{area:.3f}")
