pets = {}
k = input("Введите имя питомца: ")
k1 = input('Вид питомца: ')
k2 = int(input('Возраст питомца: '))
k3 = input('Имя владельца:  ')
pets2 = {
    'Вид питомца': k1,
    'Возраст питомца': k2,
    'Имя владельца': k3 
}
pets[k] = pets2

for key, value in pets.items():
    vid = value['Вид питомца']
    vozrast = value['Возраст питомца']
    imy = value['Имя владельца']
    year_case = ''
    if vozrast % 10 == 1 and vozrast != 11 and vozrast % 100 != 11:
        year_case = 'год'
    elif 1 < vozrast % 10 <= 4 and vozrast != 12 and vozrast != 13 and vozrast != 14:
        year_case = 'года'
    else:
        year_case = 'лет'   
print(f"Это {vid} по кличке \"{key}\". Возраст питомца: {vozrast} {year_case}. Имя владельца: {imy}")