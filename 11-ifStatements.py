x=2
y=2
if y>x:
    print("Büyüktür")
elif x==y:
    print("Eşittir")
else:
    print("Küçüktür")
    
my_City = input("Lütfen şehir adı giriniz: ")
if my_City=="Ankara":
    print(my_City+" Plaka No: "+"01")
elif my_City=="Istanbul":
    print(my_City+" Plaka No: "+"34")
elif my_City=="Diyarbakır":
    print(my_City+" Plaka No: "+"21")
elif my_City=="Izmir":
    print(my_City+" Plaka No: "+"35")
else:
    print(":( Hatalı Giriş") 
    
nationalFestivals = int(input("Nisan ayının özel günlerini öğrenmek için 1 - 30 arasında sayı giriniz: "))
if nationalFestivals==1:
    print("Şaka günü :)")
elif nationalFestivals==23:
    print("23 Ulusal Çocuk Bayramı :D")
elif nationalFestivals <1 or nationalFestivals>30:
    print("Hatalı giriş 1 - 30 arasında değer giriniz!")
else:
    print("Hatalı giriş!")
    
    
myString="Hello World! How Are You?"
if "Hello" in myString:
    print("true")
else:
    print("false")
    
myList=["a","b","c","d"]

if "c"  in myList:
    print("true")
else:
    print("false")

myDictionary={"k1":10,"k2":20,"k3":30}

if "k2" in myDictionary.keys():
    print("true")
else:
    print("false")
    
mySet=set()
mySet.add(1)
mySet.add(2)
mySet.add("a")
mySet.add("b")
print(type(mySet))
print(mySet)

if 2 in mySet:
    print("true")
else:
    print("false")
    
    
