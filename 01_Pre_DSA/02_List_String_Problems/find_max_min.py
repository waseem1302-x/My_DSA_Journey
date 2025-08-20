r_list = [5,2,7,9,8,4]

max = r_list[0]
min = r_list[0]

for i in r_list:
    if i > max:
        max = i
    elif i < min:
        min = i
print(max)
print(min)