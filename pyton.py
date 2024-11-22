dict1 = {'Russia': 'Tymen','USA': 'NY','Thailand': 'Phuket'}
dict2 = {'Russia': 'Moskov','USA': 'LA','Thailand': 'Phuket'}
set1 = {1,'Russia','Russia',2}
list1 = ('Russia','Tymen','USA','NY')

list2 = []
list3 = []
set2= set()
while dict1:
    for key,val in dict1.items():
        list2.append(key)
        list3.append(val)
        set2.add((key,val))
    break
print(f'Keys - {list2}')
print(f'Values - {list3}')
print(set2)

