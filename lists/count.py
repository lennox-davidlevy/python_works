# for value in range(1, 21):
#   print(value)

# for value in range(1, (1000**2) + 1):
#   print(value)
# list_of_a_million = []
# for value in range(0, (1000**2) + 1):
#   list_of_a_million.append(value)
# print(f"min: {min(list_of_a_million)}\n")
# print(f"max: {max(list_of_a_million)}\n")
# sum_of_a_million = sum(list_of_a_million)
# print(f"sum: {sum_of_a_million}")

# odd_numbers = []
# for value in range(1, 21, 2):
#   odd_numbers.append(value)
# print(odd_numbers)
# multiple_of_threes = []
# for value in range(3, 31, 3):
#   multiple_of_threes.append(value)
# print(multiple_of_threes)
list_of_cubes = [value**3 for value in range(1, 11)]
print(list_of_cubes)
odd_numbers = [value for value in range(1, 21, 2)]
print(odd_numbers)
multiple_of_threes = [value for value in range(3, 31, 3)]
print(multiple_of_threes)


