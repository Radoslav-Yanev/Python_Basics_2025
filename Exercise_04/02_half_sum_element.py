import sys

number_count = int(input())

biggest_num = -sys.maxsize
sum_numbers = 0

for _ in range(number_count):
    current_number = int(input())

    if current_number > biggest_num:
        biggest_num = current_number

    sum_numbers += current_number

half_num = sum_numbers - biggest_num

if half_num == biggest_num:
    print(f"Yes\nSum = {biggest_num}")
else:
    print(f"No\nDiff = {abs(half_num - biggest_num)}")