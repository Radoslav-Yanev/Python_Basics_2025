CALORIES_BURNED_PER_MINUTE = 5

walk_time_per_day = int(input())
walk_count_per_day = int(input())
calories_per_day = int(input())

calories_burned = (walk_time_per_day * CALORIES_BURNED_PER_MINUTE) * walk_count_per_day

if calories_burned >= (calories_per_day / 2):
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")

else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")