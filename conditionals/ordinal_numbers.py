num_list = list(range(1, 10))
ordinal_list = []
for num in num_list:
    if num == 1:
        ordinal_list.append(str(num) + "st")
    elif num == 2:
        ordinal_list.append(str(num) + "nd")
    elif num == 3:
        ordinal_list.append(str(num) + "rd")
    else:
        ordinal_list.append(str(num) + "th")
for num in ordinal_list:
    print(num)
