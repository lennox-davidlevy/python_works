cars = ['bmw', 'audi', 'toyota', 'subaru']
# permanent sorting
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
# temporary sorting
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"\nHere is the cars original list: \n{cars}")
print(f"\nHere is the sorted list: \n{sorted(cars)}")
print(f"\nAnd here is the list again: \n{cars}")
#reverse the list by index
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nReverse the cars")
print(cars)
cars.reverse()
print(cars)
