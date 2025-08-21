WATER_RESIST_DISTANCE = 15
WATER_RESIST_DELAY = 12.5

record_in_seconds = float(input())
distance_in_meters = float(input())
time_per_one_meter = float(input())

total_delay = (distance_in_meters // WATER_RESIST_DISTANCE) * WATER_RESIST_DELAY
total_time = (time_per_one_meter * distance_in_meters) + total_delay

if total_time < record_in_seconds:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(record_in_seconds - total_time):.2f} seconds slower.")

