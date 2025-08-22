controla_minutes = int(input())
controla_seconds = int(input())
distance_in_meters = float(input())
seconds_for_100meters = int(input())

total_controla_time = (controla_minutes * 60) + controla_seconds
delay = (distance_in_meters / 120) * 2.5

base_time = (distance_in_meters / 100) * seconds_for_100meters
total_martin_time = base_time - delay

if total_martin_time <= total_controla_time:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_martin_time:.3f}.")

else:
    difference = total_martin_time - total_controla_time
    print(f"No, Marin failed! He was {difference:.3f} second slower.")