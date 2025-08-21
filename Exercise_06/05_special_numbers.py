number = int(input())

for num in range(1111, 10_000):
    for str_num in str(num):

        if str_num == "0":
            break

        digit = int(str_num)

        if number % digit != 0:
            break
    else:
        print(num, end = " ")