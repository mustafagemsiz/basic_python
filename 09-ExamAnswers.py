# Aşağıdaki String'in 5. harfini my_letter isimli bir değişkene atayınız.

my_string = "James Hetfield"
my_letter=my_string[4]
print(my_letter)

# Aşağıdaki String'in 5. ve 8. karakteri arasındaki tüm harflerini yazdırınız (5 ve 8 dahil)

my_new_string = "QuentinTarantino"
print(my_new_string[4:8])

# Aşağıdaki String'i kod ile tersten yazın

my_last_string = "Afyonkarahisarlılaştıramadıklarımızdanmısınız"
print(my_last_string[::-1])

# Aşağıdaki işlemin sonucu hangi veri tipinde olacaktır?

print(type(3 + 10.2 + 50))
#Cevap Float

# Aşağıdaki işlemin sonucu kaçtır?

print(type(5 + 8 * 12))
#Cevap Int

# Bu listeyi 3 farklı yoldan oluşturunuz: [1,2,"a"]

# Cevap 1.a)
newList=[1,2,"a"] 
print((newList))

# Cevap 1.b)
newDict={"k1":1,"k2":2,"k3":"a"}
print(newDict.values())

# Cevap 1.c)
newSet=set()
newSet.add(1)
newSet.add(2)
newSet.add("a")

print(newSet)

# Aşağıdaki "a"'yı tek satırda alınız:
my_list = [1,4,[2,3,"a"]]
print(my_list[2][2])

# Aşağıdaki "b"'yi tek satırda alınız:
my_dictionary = {"k1":2, "kk":[4,{"kkkk":"b"}]}

print(my_dictionary["kk"][1]["kkkk"])

# Aşağıdaki liste set'e çevirilince hangi değerler içinde kalacaktır?

my_list_to_be_set = [11,12,22,33,11,22,45,32,21,22,33,45]

# Cevap 11, 12, 22, 33, 45, 32, 21

# Aşağıdaki ifadenin sonucu ne olacaktır?

x = 40 * 5 + 3

y = 208 - 2 * 4

print(x > y)

# Cevap True

# Aşağıdaki ifadenin sonucu ne olacaktır?

a = 40 * (4 - 2)

b = 80 - 2 * -5

print(a > b)

# Cevap False




