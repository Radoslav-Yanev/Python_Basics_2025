from math import floor

record = float(input())
distance = float(input())
time_per_1meter = float(input())

delay_count = floor(distance / 50)
total_delay_time = delay_count * 30
total_time = (distance * time_per_1meter) + total_delay_time

if total_time < record:
    print(f" Yes! The new record is {total_time:.2f} seconds.")

else:
    print(f"No! He was {abs(record - total_time):.2f} seconds slower.")