pages_count = int(input())
pages_for_hour = int(input())
day_count = int(input())

total_time = pages_count // pages_for_hour

hour_needed = total_time // day_count

print(hour_needed)