my_list = [10,20,30,40,50,60]

for number in my_list:
    print(number * 5)

for num in my_list:
    if num == 30:
        break  #30 a gelince işlemi sonlandır
    print(num * 5)

for item in my_list:
    if item == 30:
        continue  #30 u atla işleme devam et
    print( item * 5)

for no in my_list:
    pass # hiç birşey yapma devam et