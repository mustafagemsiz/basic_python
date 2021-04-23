#tupl özelliği içindeki değerleri değiştirilemez olduğundan gelir.

myTuple=tuple()
myTuple=(1,2,2,2,2,2,3,4,"a","b")
print(type(myTuple))

print(myTuple[2])
myTuple[3]=5 #burada hata verecektir sebebi değerlerin değiştirilemezliği
print(myTuple)

print(myTuple.count(2)) #burada listede kaç tane 2 var diye saydırmasını istedik sonuc=5

