import sys

n = int(input())
biggest_num = -sys.maxsize
smallest_num = sys.maxsize

for i in range(n):
    number = int(input())

    if number > biggest_num:
        biggest_num = number

    if number < smallest_num:
        smallest_num = number

print(f"Max number: {biggest_num}")
print(f"Min number: {smallest_num}")




