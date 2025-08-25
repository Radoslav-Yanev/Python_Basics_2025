import sys; from math import ceil

ONE_PACAGE_SUGAR_IN_GR = 950
ONE_PACAGE_FLOUR_IN_GR = 750

easter_bread_count = int(input())

total_sugar = 0
total_flour = 0
max_quantity_flour =  - sys.maxsize
max_quantity_sugar = - sys.maxsize

for _ in range(easter_bread_count):
    used_sugar_quantity = int(input())
    used_flour_quantity = int(input())

    if used_sugar_quantity > max_quantity_sugar:
        max_quantity_sugar = used_sugar_quantity

    if used_flour_quantity > max_quantity_flour:
        max_quantity_flour = used_flour_quantity

    total_sugar += used_sugar_quantity
    total_flour += used_flour_quantity

sugar_needed_packages = total_sugar / ONE_PACAGE_SUGAR_IN_GR
flour_needed_packages = total_flour / ONE_PACAGE_FLOUR_IN_GR

print(f"Sugar: {ceil(sugar_needed_packages)}")
print(f"Flour: {ceil(flour_needed_packages)}")
print(f"Max used flour is {max_quantity_flour} grams, max used sugar is {max_quantity_sugar} grams.")
