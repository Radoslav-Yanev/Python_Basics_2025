from math import ceil

serial_name = input()
serial_duration = int(input())
break_duration = int(input())

retreat_duration = break_duration * 0.25
lunch_duration = break_duration * 0.125

total_time = (retreat_duration + lunch_duration + serial_duration)

if total_time <= break_duration:
    print(f"You have enough time to watch {serial_name} and left with {ceil(break_duration - total_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(total_time - break_duration)} more minutes.")