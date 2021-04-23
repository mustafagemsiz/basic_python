    #Range
for i in range(-20,21):
    print(i)
    
print(list(range(0,21)))
    
for a in range(10):
    print(a*5)
    
    
   #Enumerate index değerini yazdırır
for number in enumerate(range(3,7)):
    print(number)
   
#Random rastgele sayı üretir  
from random import randint
print(randint(0,100))
print(randint(0,100))



#Shuffle karıştırma işine yarar
from random import shuffle
myList= [1,2,3,4,5,6,7,8,9,10]
shuffle(myList)
print(myList)

from random import shuffle
myList2=list(range(0,10))
shuffle(myList2)
print(myList2)

#Zip birleştirme işlemine yarar

ad=["ali","ahmet","ela","lale"]
soyad=["yılmaz","fidan","şahin","demir"]
yas=[22,23,21,25]
newList=list(zip(ad,soyad,yas))#list(zip())
print(newList)
for users in newList:
    print(users)
    
#List advanced
newList3=[]
myString="Hoşgeldiniz"
for new in myString:
    newList3.append(new*2)
print(newList3)

myString2="Hoşgeldiniz"
newList4= [new2*2 for new2 in myString2]
print(newList4)

myNumberList=list()
myNumber=1,2,3,4,5
myNumberList=[newNumber*5 for newNumber in myNumber]
print(myNumberList)




