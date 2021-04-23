text="Hello World!"
print(text)

#metin ler 0 dan başlar

#text e bağlı değerin 0 ıncı değerini getirir.
print(text[0])

#text e bağlı değerin 4 üncü değerini getirir.
print(text[4])

#text e bağlı değerin -1 inci değerini getirir ama sondan itibaren almaya başlar.
print(text[-1])

number="1243567890"
#number değerini 2 inci index ten sonra getir bu işlene kesme yani slicing işlemi denir.
print(number[2:])

#number değerini 2 inci index ten önce getir buna 2 te dahil.

print(number[:2])

#number değerini 2 inci index ten sonra 6 ya kadar 6 dahil getir.
print(number[2:6])

#2.şer 2.şer atla ve getir
print(number[::2])

#3.er 3.er atla ve getir
print(number[::3])

#değerleri tersten getirir
print(number[::-1])

#----------------------------------------------------------------------------------------#

text3="mustafa"
print(text3)
print(text3.capitalize()) #baş harfi büyük yazdırır.

text4="mustafa birhat gemsiz"
print(text4.split()) #her kelimeyi ayırır

print(text4.upper()) #tüm harfleri büyük yazdırır