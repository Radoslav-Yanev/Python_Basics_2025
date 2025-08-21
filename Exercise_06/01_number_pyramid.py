n = int(input())

is_max_num = False
counter = 0

for row in range(1, n + 1):
    for _ in range(row):
        counter += 1
        print(counter, end=" ")

        if counter == n:
            is_max_num = True
            break

    if is_max_num:
        break

    print()