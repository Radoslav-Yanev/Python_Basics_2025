import sys

bigger_integer = -sys.maxsize

while True:
    new_input = input()

    if new_input == "Stop":
        break

    number = int(new_input)

    if number > bigger_integer:
        bigger_integer = number

print(bigger_integer)





