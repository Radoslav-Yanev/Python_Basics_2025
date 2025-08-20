numbers = int(input())
even_sum = 0
odd_sum = 0

for idx in range(numbers):
    new_number = int(input())

    if idx % 2 == 0:
        even_sum += new_number
    else:
        odd_sum += new_number

if even_sum == odd_sum:
    print(f"Yes\nSum = {even_sum}")
else:
    print(f"No\nDiff = {abs(even_sum - odd_sum)}")