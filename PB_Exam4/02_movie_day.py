photo_time = int(input())
stages_count = int(input())
stage_duration = int(input())

prepare_time = photo_time * 0.15
total_time = (stage_duration * stages_count) + prepare_time

if photo_time >= total_time:
    print(f"You managed to finish the movie on time! You have {round(photo_time - total_time)} minutes left!")

else:
    print(f"Time is up! To complete the movie you need {round(total_time - photo_time)} minutes.")
