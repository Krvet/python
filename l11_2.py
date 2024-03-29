import collections
from imaplib import Commands
pets = {
    1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"
            },
        },
}
 
def create():
    key = input("Кличка питомца: ")
    field = ["Вид питомца","Возраст питомца","Имя владельца"]
    temp = {key: dict()}
    for fiel in field:
        res = input(f'{fiel}:')
        temp[key][fiel] = int(res) if res.isnumeric() else res
    last = collections.deque(pets, maxlen=1)[0]
    pets[last + 1] = temp

def read():
    ID = int(input("Введите ID: "))
    pet = get_pet(ID)
    if not pet:
        print(f"Нет питомца с таким ID:{ID}")
        return
    key = [x for x in pet.keys()][0]
    string = f'Это {pet[key]["Вид питомца"]} по кличке "{key}". ' \
    f'Возраст питомца: {pet[key]["Возраст питомца"]} {get_suffix(pet[key]["Возраст питомца"])}. ' \
    f'Имя владельца: {pet[key]["Имя владельца"]}'
    print(string)

def update():
    ID = int(input("Введите ID: "))
    pet = get_pet(ID)
    if not pet:
        print(f"Нет питомца с таким ID:{ID}")
        return
    kkey = [x for x in pet.keys()][0]
    print("Введите данные или оставьте поле пустым. Нажмите Enter")

    temp = dict()
    for key, value in pet[kkey].items():
        res = input(f"{key}: ")
        if res:
            temp[key] = int(res) if res.isnumeric() else res

    pet[kkey].update(temp)

def delete():
    ID = int(input("Введите ID: "))
    pets.pop(ID, None)

def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False

def get_suffix(age):
    if age % 10 == 1 and age != 11 and age % 100 != 11:
        return 'год'
    elif 1 < age % 10 <= 4 and age != 12 and age != 13 and age != 14:
        return 'года'
    return 'лет'

def pets_list():
    for key, val in pets.items():
        print(f"ID:{key}", val)

commands = {
    "create": create,
    "read": read,
    "update": update,
    "delete": delete,
    "list": pets_list,
    "stop": 0
}

def print_commands():
    print("Список доступных комманд:")
    for key in commands:
        print("> ", key)
    while True:
        command = input("Введите команду: ")
        if command not in commands.keys():
            continue
        if command == "stop":
            break
        commands[command]()
        input("Продолжить...")

print_commands()
