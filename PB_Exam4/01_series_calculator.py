from math import floor

series_name = input()
seasons_count = int(input())
episodes_count = int(input())
normal_episode_without_ads = float(input())

episode_with_ads = normal_episode_without_ads + (normal_episode_without_ads * 0.20)
special_episode = seasons_count * 10

total_time = ((episode_with_ads * episodes_count) * seasons_count) + special_episode

print(f"Total time needed to watch the {series_name} series is {floor(total_time)} minutes.")


