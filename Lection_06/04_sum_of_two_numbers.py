start = int(input())
end = int(input())
magic_number = int(input())

is_found = False
combinations = 0

for first_num in range(start, end+1):
    for second_num in range(start, end+1):

        combinations += 1

        if first_num + second_num == magic_number:
            is_found = True
            print(f"Combination N:{combinations} ({first_num} + {second_num} = {magic_number})")
            break

    if is_found:
        break

if not is_found:
    print(f"{combinations} combinations - neither equals {magic_number}")