cake_size = int(input()) * int(input())

count_pieces = 0
is_left = False

while cake_size > count_pieces:
    pieces = input()

    if pieces == "STOP":
        is_left = True
        break

    count_pieces += int(pieces)

if is_left:
    print(f"{cake_size - count_pieces} pieces are left.")

else:
    print(f"No more cake left! You need {count_pieces - cake_size} pieces more.")