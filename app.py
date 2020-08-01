data1 = ['João', 'Maria', 'Pelé']
data2 = ['Vagner', 'Djalma', 'João', 'Maria', 'Agenor', 'Pelé']
data_copy2 = data2

for el in data1:
     if el in data_copy2:
         data_copy2.remove(el)
print(data_copy2)


data1 = ['João','Maria','Pelé']
data2 = ['Vagner','Djalma','João','Maria','Agenor','Pelé']
set1, set2 = set(data1), set(data2)
printList = list(set1.symmetric_difference(set2))
print(printList)