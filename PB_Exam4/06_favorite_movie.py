import sys

film_count = 0
best_film_name = ""
best_film_value = - sys.maxsize

while True:
    film_name = input()

    if film_name == "STOP":
        break

    film_count += 1

    if film_count == 7:
        print(f"The limit is reached.")
        break

    film_symbols_sum = 0

    for char in film_name:
        film_symbols_sum += ord(char)

        if char.islower():
            film_symbols_sum -= len(film_name) * 2

        elif char.isupper():
            film_symbols_sum -= len(film_name)

    if film_symbols_sum > best_film_value:
        best_film_value = film_symbols_sum
        best_film_name = film_name

print(f"The best movie for you is {best_film_name} with {best_film_value} ASCII sum.")