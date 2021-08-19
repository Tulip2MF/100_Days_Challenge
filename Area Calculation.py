""" One can paint 5square meters of wall with one can.
Now give the program to calculate the number of can required for a given area
"""
import math


def area_calculator(height, width, coverage):
    paint = height * width / coverage
    bottle = math.ceil(paint)
    return bottle


wall_height = float(input("What is the height of the wall in meters? "))
wall_width = float(input("What is the width of the wall in meters? "))
paint_bottle = area_calculator(coverage=5, height=wall_height, width=wall_width)
print(f"You will need {paint_bottle} bottles.")
