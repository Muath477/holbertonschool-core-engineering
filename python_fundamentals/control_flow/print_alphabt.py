#!/usr/bin/env python3
alphabet = ""

for i in range(97, 123):
    letter = chr(i)
    if letter != 'q' and letter != 'e':
        alphabet += letter

print("{}".format(alphabet), end="")
