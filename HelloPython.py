#imports
from random import randrange as rand
from time import sleep

#driver code
def print_string(current_string, expected_character):
    while True:
        some_random_character = rand(0, 127)
        print("\r" + current_string + chr(some_random_character), end="")
        sleep(0.1)  # Comment this line to see the result instantly
        if chr(some_random_character) == expected_character:
            break

#byte code
my_string = "Hello World"
current_str = ""
for letter in my_string:
    print_string(current_str, letter)
    current_str += letter
