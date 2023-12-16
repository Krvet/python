text = (input("Введите слово: ")) 
a = text.count('a') 
e = text.count('e') 
i = text.count('i') 
o = text.count('o') 
u = text.count('u') 

if a == 0: 
    print("a = False") 
if e == 0: 
    print("e = False") 
if i == 0: 
    print("i = False") 
if o == 0: 
    print("o = False") 
if u == 0: 
    print("u = False") 

print(f"Гласных: {a + e + i + o + u}") 
print(f"Согласных:{len(text) - (a + e + i + o + u)}")

