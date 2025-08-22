goal_heigh = int(input())

bar_heigh = goal_heigh - 30
jumps_count = 0
fails = 0

while True:
    current_jump = int(input())
    jumps_count += 1

    if current_jump > bar_heigh:
        bar_heigh += 5
        fails = 0

    else:
        fails += 1
        if fails == 3:
            print(f"Tihomir failed at {bar_heigh}cm after {jumps_count} jumps.")
            break

    if bar_heigh > goal_heigh:
        print(f"Tihomir succeeded, he jumped over {goal_heigh}cm after {jumps_count} jumps.")
        break


# SECOND WAY

# heigh_goal = int(input())
#
# bar_heigh = heigh_goal - 30
# jumps_count = 0
# fails = 0
#
# while True:
#     current_jump_height = int(input())
#     jumps_count += 1
#
#     if current_jump_height > bar_heigh:
#         bar_heigh += 5
#         fails = 0
#
#         if bar_heigh > heigh_goal:
#             print(f"Tihomir succeeded, he jumped over {heigh_goal}cm after {jumps_count} jumps.")
#             break

#     else:
#         fails += 1
#         if fails == 3:
#             print(f"Tihomir failed at {bar_heigh}cm after {jumps_count} jumps.")
#             break
