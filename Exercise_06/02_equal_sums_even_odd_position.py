num1 = int(input())
num2 = int(input())

for number in range(num1, num2 + 1):
    even_sum = 0
    odd_sum = 0

    for index, value in enumerate(str(number)):

        if value == "0":
            continue

        if index % 2 == 0:
            even_sum += int(value)
        else:
            odd_sum += int(value)

    if even_sum == odd_sum:
        print(number, end=" ")