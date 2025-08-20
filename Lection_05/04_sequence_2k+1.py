n = int(input())

next_num = 0

while True:
    next_num = (next_num * 2) + 1

    if next_num > n:
        break
    print(next_num)