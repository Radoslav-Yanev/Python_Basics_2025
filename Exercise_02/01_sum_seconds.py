time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time_in_seconds = time_first + time_second + time_third

hours = total_time_in_seconds // 60
minutes = total_time_in_seconds % 60

if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")