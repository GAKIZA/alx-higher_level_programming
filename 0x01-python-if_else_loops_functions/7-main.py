#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else"upper"))
print("A is {}".format("lower" if islower("W") else "upper"))
print("a is {}".format("lower" if islower("a") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))
