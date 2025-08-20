n = int(input())
left_number = 0
right_number = 0

for idx in range(n * 2):
    new_number = int(input())

    if idx < n:
         left_number += new_number
    else:
        right_number += new_number

if left_number == right_number:
    print(f"Yes, sum = {left_number}")
else:
    print(f"No, diff = {abs(left_number - right_number)}")
