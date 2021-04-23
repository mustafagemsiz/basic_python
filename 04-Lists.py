myList=["ali","ayşe","fatma"]
myList.append("Talat") #listeye değer ekleme
print(myList[3]) #listeden istenilen değeri çağırma
myList.reverse()#listeyi tersine çevirir
print(myList)

print("---------"*4)

myNumber=[1,2,3,4,5]
myNumber.append(6)
print(myNumber[5])

print("---------"*4)

myMixList = myList + myNumber

print(myMixList)

print("---------"*4)

#iç içe dizi işlemleri

firstList=[1,2,3,"a","b",[4,5,"c"]]

#dizi içindeki diziye ermişmenin birinci yöntemi
print(firstList[5][2])

#dizi içindeki diziye ermişmenin ikinci yöntemi
newList = firstList[5]
print(newList[2])

print(firstList[4:]) #4. indexten sonrasını al

print(firstList[:4]) #4. index dahil öncesini al
