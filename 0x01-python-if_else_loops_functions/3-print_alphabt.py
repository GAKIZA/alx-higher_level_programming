#!/usr/bin/python3

for letter_code in range(97, 123):
    if chr(letter_code) == 'e' or chr(letter_code) == 'q':
        continue
    else:
        print("{}".format(chr(letter_code)), end="")
