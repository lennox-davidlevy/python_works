motorcycles = ['honda', 'yamaha', 'suzuki']

#add to end of list: append
motorcycles.append('dukati')

#insert in to list by index
motorcycles.insert(0, 'harley davidson')
motorcycles.insert(1, 'huffy')
for bike in motorcycles:
  print(bike.title())

#pop off end of the list
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle, motorcycles)

first_owned = motorcycles.pop(0)
print("first_owned:", first_owned, motorcycles)

motorcycles.remove('suzuki')
print(motorcycles)
motorcycles.append('dukati')
too_expensive = 'dukati'
motorcycles.remove(too_expensive)
print(f"\nA {too_expensive.title()} is too expensive for me")
