import math


def find_middle(input_list):
    middle = float(len(input_list)) / 2
    if middle % 2 != 0:
        return int(middle - 0.5)
    else:
        return int(middle)


bicycles = ["trek", "cannondale", "redline", "specialized", "huffy", "ambush"]
mid = find_middle(bicycles)
print(f"Full list of bicycles: {bicycles}")
print(f"The first three items in this list are: {bicycles[:3]}\n")
print(f"Three middle items: {bicycles[mid-1:mid+2]}\n")
print(f"Three last items: {bicycles[-3:]}\n")
