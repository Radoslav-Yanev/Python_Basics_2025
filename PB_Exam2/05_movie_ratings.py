import sys

movie_count = int(input())

the_biggest_rating = - sys.maxsize
the_lowest_rating = sys.maxsize
biggest_rating_movie_name = ""
lowest_rating_movie_name = ""
total_rating = 0

for _ in range(movie_count):
    film_name = input()
    film_rating = float(input())

    if film_rating >the_biggest_rating:
        the_biggest_rating = film_rating
        biggest_rating_movie_name = film_name

    elif film_rating < the_lowest_rating:
        the_lowest_rating = film_rating
        lowest_rating_movie_name = film_name

    total_rating += film_rating

average_rating = total_rating / movie_count

print(f"{biggest_rating_movie_name} is with highest rating: {the_biggest_rating:.1f}")
print(f"{lowest_rating_movie_name} is with lowest rating: {the_lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
