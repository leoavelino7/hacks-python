data1 = [20,30,40,40,30,50,60,50]
data_copy = []
for el in data1:
    if el not in data_copy:
        data_copy.append(el)
print(data_copy) # [20, 30, 40, 50, 60]

data1 = [20,30,40,40,30,50,60,50]
list_set = list(set(data1))
print(list_set) # [40, 50, 20, 60, 30]