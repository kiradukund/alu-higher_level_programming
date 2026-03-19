#!/usr/bin/python3
roman_to_int = __import__('12-roman_to_int').roman_to_int
for r in ["X", "VII", "IX", "LXXXVII", "DCCVII"]:
    print("{} = {}".format(r, roman_to_int(r)))
