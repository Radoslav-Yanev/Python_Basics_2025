from math import floor
import sys

vowels = {"a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"}

max_word_sum = - sys.maxsize
max_word = ""

while True:
    word = input()

    if word == "End of words":
        break

    current_word_sum = 0

    for char in word:

        current_word_sum += ord(char)

    first_char = word[0]

    if first_char in vowels:
        current_word_sum *= len(word)

    else:
        current_word_sum = floor(current_word_sum / len(word))

    if current_word_sum > max_word_sum:
        max_word_sum = current_word_sum
        max_word = word

print(f"The most powerful word is {max_word} - {max_word_sum}")





