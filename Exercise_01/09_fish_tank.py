length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

aquarium_volume = length * width * height
volume_in_litters = aquarium_volume / 1000
needed_litters = volume_in_litters - (volume_in_litters * percent)

print(needed_litters)