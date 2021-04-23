

my_list = [1,2,3,4,5]

for number in my_list:
    print(number)

for item in my_list:
    new_number = item * 5
    print(new_number)

for number in my_list:
    if number % 2 == 0:
        print(number)

if 2 in my_list:
    print("true")

for num in my_list:
    if num == 2:
        print("true")

my_string = "James Hetfield"

for letter in my_string:
    print(letter)

my_tuple = (1,2,3)

for item in my_tuple:
    print(item * 5 - 10)

my_new_list = [("a","b"),("c","d"),("e","f"),("g","h")]

for element in my_new_list:
    print(element)

for (x,y) in my_new_list:
    print(x)
    print(y)

my_tuple_list = [(0,1,2),(3,4,5),(9,10,11)]

for (x,y,z) in my_tuple_list:
    print(z)


my_dictionary = {"key1": 100, "key2" : 200, "key3" : 300}

for (key,value) in my_dictionary.items():
    print(key)
    
    
myExe=["camtasia","ps6","discord","skype"]
for exe in myExe:
    print(exe+".exe")
    
    myExec=["camtasia..exe","ps6","discord","skype"]
for testExe in myExec:
    if ".exe" in testExe:
        print(testExe)
    else :
        print(testExe+".exe")
        
        