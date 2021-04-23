
#set lerde veriler .add ile eklenir
#list lerde .append ile eklenir
#dict lerde standar myDict["key1"] = 1 diye eklenir.

myList= [1,2,3,1,1,2,2,2,2]
myList.append(3)
myList.append(4)
newList=set((myList))
print(newList)
print(type(newList))

print("-" * 15)

mySet=set()
mySet.add(1)
mySet.add(1)
mySet.add(2)
mySet.add(3)
print(mySet)
print(type(mySet))

print("-" * 15)

my_List=list()
print(type(myList))
my_List.append(1)
my_List.append(8)
my_List.append(3)
my_List.append([8,9])
print(my_List)
print(my_List)

my_dict_2 = dict()
my_dict_2["key1"] = 1
print(my_dict_2)

