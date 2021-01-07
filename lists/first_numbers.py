num_list = ['zeroth', 'first', 'second', 'third', 'fourth']


# for value in range(0, 5):
#   print(num_list[value].title())

numbers = list(range(0,10))
# print(numbers)

# range(start, end, step)
even_numbers = list(range(2, 11, 2))
# print(even_numbers)

squares = []
# for value in range(1, 11):
#   square = value ** 2
#   squares.append(square)
# print(squares)

for value in range(1, 11):
  squares.append(value ** 2)
# print(squares)

digits = range(0, 10)
digits_list = []
for value in range(0, 10):
  digits_list.append(value)

print(f"min: {min(digits)}\n")
print(f"max: {max(digits)}\n")
print(f"sum: {sum(digits)}\n")