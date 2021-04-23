myDictionary={"key":"value"}
print(myDictionary["key"])

newDictionary={"Grafiker":"Şevval","Pentester":"Mustafa"}
print(newDictionary["Grafiker"])

myDictionary2={"ad":"Ali","yas":21}
print(myDictionary2["yas"])


myDictionary3={"key1":100,"key2":[10,20,30],"key3":{"a":5}}
print(myDictionary3.keys())
print(myDictionary3.values())
print(myDictionary3["key2"][1])
print(myDictionary3["key3"]["a"])


myDictionary4 = {"k1":1,"k2":2}

myDictionary4["k1"]=11 #düzenleme işlemi
myDictionary4["k3"]=3 #ekleme işlemi

print(myDictionary4)