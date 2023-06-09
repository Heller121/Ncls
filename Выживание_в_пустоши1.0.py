import random
import time

player = {
    'Имя': "",
    "Оружие": 0,
    "Максимальное здоровье": 100,
    "Здоровье": 100,
    "Сила": 13,
    "Уровень": 1,
    "Опыт": 0,
    "Защита": 5,
    "Ваши вещи": [],
    "Количество денег": 0,
    "Атака": [0, 0]  # начальное значение атаки
}

p = 0

#Словарь с оружием у игрока
player["Оружие"] = {
    "название": "Мачете",
    "Атака": [8, 12],
    "описание": "Старый добрый мачете, сделанный из твердой,довоенной стали.",
    "стоимость": 100
}

weapons = [
{"название":"Ножик","Атака": [3, 8],"описание": "Уже ржавый,но всё еще рабочий острый нож.","стоимость":30},
{"название":"Бита","Атака": [2, 10],"описание": "Немного обгоревшая старая бейсбольная бита.","стоимость":32},
{"название":"Кинжал","Атака": [4, 7],"описание": "Уже ржавы,но всё еще рабочий острый нож.","стоимость":20}
    ]

items= [
{"название": "журнал", "описание": "старый журнал про путешествия","стоимость":2},
{"название": "пачка риса", "описание":"картонная упаковка риса,название стеёрлось","стоимость":5},
{"название": "бинт","описание":"довоенный бинт,используется для восстановления здоровья","стоимость":10,"эффект":{"лечение": 20}},
{"название": "бутылка воды","описание":"стеклянная бутылка с грязной водой,маркировка стёрта недавно","стоимость":7},
{"название": "книга","описание":"потертая книга,на которой частично виднеется название:'у_о без_тн_с жи_яль___ти'","стоимость":4},
{"название": "таблетки","описание":"пачка просроченных обезболивающих таблеток","стоимость":16,"эффект":{"лечение": 30}}
]

enemies = [
    {"наименование врага": "Заражённая крыса", "Здоровье": 4, "Сила": 5, "Защита": 0,"Описание":"грызун,заражённый неизвестным вирусом","Опыт":10,"Количество денег":0},
    {"наименование врага": "Огромный таракан", "Здоровье": 16, "Сила": 10, "Защита": 2,"Описание":"огромное насекомое,способное быстро передвигаться","Опыт":15,"Количество денег":0},
    {"наименование врага": "Урод", "Здоровье": 30, "Сила": 15, "Защита": 5,"Описание":"человек,облучённый радиацией и подвергшийся сгниванию мозгов","Опыт":20,"Количество денег":10},
    {"наименование врага": "Рейдер", "Здоровье": 50, "Сила": 30, "Защита": 8,"Описание":"человек,насилующий и убивающий в поисках ценностей,безбашенный и опасный ублюдок","Опыт":30,"Количество денег":20},
    {"наименование врага": "Военный", "Здоровье": 80, "Сила": 50, "Защита": 15,"Описание":"бывший военный, а ныне вооруженный преступник. Очень опасен и защищён","Опыт":45,"Количество денег":50}
]

#Создание игрока

def create_player():
    player_name = input("Как тебя зовут? ")
    player["Имя"] = player_name
    print(f"Добро пожаловать в Пустошь, {player_name}!")
    print("Имя:", player["Имя"]) # изменение вывода имени без скобок и кавычек
create_player()

#Атака
def attack():
    player["Атака"] = [8, 12]  # задаем новое значение атаки
    print("Атака:", player["Атака"][0], "-", player["Атака"][1]) # изменение вывода атаки без скобок и кавычек

#Статистика
def show_player_stats():
    print("--------------------------------------------------------------------------------")
    time.sleep(0.3)
    print("Статистика игрока:")
    time.sleep(0.3)
    print("Деньги:",player["Количество денег"])
    time.sleep(0.3)
    print("Уровень:", player["Уровень"]) # изменение вывода уровня без скобок и кавычек
    time.sleep(0.3)
    print("Опыт:", player["Опыт"]) # изменение вывода опыта без скобок и кавычек
    time.sleep(0.3)
    print("Здоровье:", player["Здоровье"], "/", player["Максимальное здоровье"]) # изменение вывода здоровья без скобок и кавычек
    time.sleep(0.3)
    print("Максимальное здоровье:", player["Максимальное здоровье"]) # изменение вывода максимального здоровья без скобок и кавычек
    time.sleep(0.3)
    print("Атака:", player["Атака"][0], "-", player["Атака"][1]) # изменение вывода атаки без скобок и кавычек
    time.sleep(0.3)
    print("Оружие:")
    time.sleep(0.3)
    if player["Оружие"]:
        time.sleep(0.3)
        print(player["Оружие"]["название"], ":", player["Оружие"]["описание"], ", бонус к атаке:", player["Оружие"]["Атака"], ", оно стоит:", player["Оружие"]["стоимость"]) # изменение вывода оружия без скобок и кавычек
    else:
        print("У вас нет оружия.")
        time.sleep(0.5)
     
    print("--------------------------------------------------------------------------------")
    #Открытие рюкзака
def show_items():
    print("Рюкзак:")
    for i, item in enumerate(player["Ваши вещи"]): # Использование функции enumerate для отображения индексов элементов
        print(f"{i + 1}. {item['название']}: {item['описание']}, стоимость: {item['стоимость']}")
        if 'эффект' in item:
            for effect_name, effect_value in item['эффект'].items():
                print(f"Эффект: {effect_name}, значение: {effect_value}")
    if not player["Ваши вещи"]:
        print("Ваш рюкзак пуст.")

#Покупка предметов в магазине
def buyed_items():
    print("Доступные предметы:")
    for i, item in enumerate(items):
        print(f"{i + 1}. {item['название']} ({item['стоимость']} монет)")

def buy_item():
    print("1. ЖУРНАЛ,старый журнал про путешествия,СТОИМОСТЬ: 2")
    time.sleep(1)
    print("2. ПАЧКА РИСА, картонная упаковка риса,название стёрлось,СТОИМОСТЬ: 5.")
    time.sleep(1)
    print("3. БИНТ,довоенный бинт,используется для восстановления здоровья,СТОИМОСТЬ: 10,ЭФФЕКТ-лечение: 20 ед.зд.")
    time.sleep(1)
    print("4. БУТЫЛКА ВОДЫ,стеклянная бутылка с грязной водой,маркировка стёрта недавно,СТОИМОСТЬ: 7.")
    time.sleep(1)
    print("5. КНИГА,потертая книга,на которой частично виднеется название:'у_о без_тн_с жи_яль___ти,СТОИМОСТЬ: 4.")
    time.sleep(1)
    print("6. ТАБЛЕТКИ,пачка просроченных обезболивающих таблеток,СТОИМОСТЬ: 16,ЭФФЕКТ-лечение: 30 ед.зд. ")
    time.sleep(1)
    item_index = int(input("Введите номер предмета, который вы хотите купить: ")) - 1
    time.sleep(1)
    if item_index < 0 or item_index >= len(items):
        print("Некорректный номер предмета.")
        return
    item = items[item_index]
    if player["Количество денег"] < item["стоимость"]:
        print("У вас недостаточно денег, чтобы купить этот предмет.")
        return
    player["Количество денег"] -= item["стоимость"]
    player["Ваши вещи"].append(item)
    print(f"Вы купили {item['название']} за {item['стоимость']} монет.")
    print("Теперь ваш рюкзак выглядит так:")
    show_items()



#Продажа предмета в магазине
def sell_item():
    if not player["Ваши вещи"]:
        print("В вашем рюкзаке нет предметов.")
        return
    
    print("Выберите номер предмета для продажи:")
    show_items()
    item_index = int(input()) - 1
    
    if item_index < 0 or item_index > len(player["Ваши вещи"]):
        print("Неверный номер предмета.")
        return
    
    item = player["Ваши вещи"][item_index]
    player["Количество денег"] += item["стоимость"]
    player["Ваши вещи"].pop(item_index)
    
    print(f"Вы продали {item['название']} за {item['стоимость']} монет.")
    print("Теперь ваш рюкзак выглядит так:")
    show_items()

#Покупка оружия
def buy_weapon(weapon_index):
    weapons = [
        {"название": "Ножик", "атака": [3, 8], "описание": "Уже ржавый,но всё еще рабочий острый нож.", "стоимость": 30},
        {"название": "Бита", "атака": [2, 10], "описание": "Немного обгоревшая старая бейсбольная бита.", "стоимость": 32},
        {"название": "Кинжал", "атака": [4, 7], "описание": "Уже ржавы,но всё еще рабочий острый нож.", "стоимость": 20}
    ]
    weapon = weapons[weapon_index]
    if player["Количество денег"] < weapon["стоимость"]:
        print("У вас недостаточно денег, чтобы купить это оружие.")
        return
    player["Количество денег"] -= weapon["стоимость"]
    player["Оружие"].append(weapon)
    print(f"Вы купили {weapon['название']} за {weapon['стоимость']} монет.")
    print("Теперь ваше оружие выглядит так:")
    for weapon in player["Оружие"]:
        print(f"{weapon['название']}: {weapon['описание']}, атака: {weapon['атака']}")

#Нахождение предмета
def new_item():
    newitem = random.choice(items)
    print(f"Вы обнаружили: {newitem['название']}, это {newitem['описание']}")
    time.sleep(1)
    choice = input("Хотите положить эту вещь в рюкзак? [y/любой символ]: ")
    if choice == "y":
        player["Ваши вещи"].append(newitem)
        time.sleep(1)
        print(f"{newitem['название']} добавлен в рюкзак.")
    else:
        time.sleep(1)
        print("Вы оставляете эту вещь.")

#Использование предметов
def select_item():
    while True:
        show_items()
        choice = input("Выберите предмет из рюкзака или введите 'q' для выхода: ")
    if choice == 'q':
            return
    try:
            index = int(choice)
            item = player["Ваши вещи"][index]
            print(f"Выбранный предмет: {item['название']}")
            action = input("Выберите действие для этого предмета: 1 - выбросить, 2 - использовать, q - вернуться: ")
            if action == '1':
                del player["Ваши вещи"][index]
                print(f"{item['название']} выброшен.")
            elif action == '2':
                if "лечение" in item:
                    player["Здоровье"] += min(item["лечение"] + item["лечение"],100)
                print(f"{item['название']} использован.")
            elif action == 'q':
                pass
            else:
                print("Некорректный ввод.")
    except (ValueError, IndexError):
            print("Некорректный ввод.")

def losing():
    print("Вы померли!")
    exit()

def win(enemy): 
    print(f"Вы победили {enemy['наименование врага']}!") 
    time.sleep(1) 
    found_money = enemy['Количество денег']  # сохраняем количество денег от врага в отдельную переменную 
    player["Количество денег"] += found_money 
    time.sleep(1) 
    print(f"Вы находите {found_money} денег.") 
    found_exp = enemy['Опыт']  # сохраняем количество опыта от врага в отдельную переменную 
    player["Опыт"] += found_exp 
    time.sleep(1) 
    print(f"Вы получаете {found_exp} очков опыта.") 
    # Проверка на получение нового уровня 
    if player["Опыт"] >= 50: 
        player["Уровень"] = 2 
        print("Вы достигли 2-го уровня!") 
    elif player["Опыт"] >= 100: 
        player["Уровень"] = 3 
        print("Вы достигли 3-го уровня!") 
    elif player["Опыт"] >= 150: 
        player["Уровень"] = 4 
        print("Вы достигли 4-го уровня!") 
    elif player["Уровень"] == "4": 
        print("До свидания!") 
        exit()

def battle(enemy):
    print(f"Вы столкнулись с {enemy['наименование врага']}! Это {enemy['Описание']}")
    while player['Здоровье'] > 0 and enemy['Здоровье'] > 0:
        print(f"{player['Имя']} Здоровье: {player['Здоровье']}")
        time.sleep(2)
        print(f"{enemy['наименование врага']} Здоровье: {enemy['Здоровье']}")
        time.sleep(2)
        options = ["ударить", "выбрать оружие", "сбежать"]
        print("Выберите действие:", options)
        action = input()
        while action not in options:
            print("Неправильный ввод, выберите действие:", options)
            action = input()
        if action == "сбежать":
            chance = random.randint(0, 1)
            if chance == 0:
                print(f"{player['Имя']} не удалось сбежать!")
                time.sleep(2)
                enemy_attack = enemy["Сила"] + random.randint(-2, 2)
                player_defence = player["Защита"] + random.randint(-1, 1)
                damage = max(enemy_attack - player_defence, 0)
                print(f"{enemy['наименование врага']} атаковал {player['Имя']} на {damage} урона!")
                time.sleep(2)
                player["Здоровье"] -= damage
                if player["Здоровье"] <= 0:
                    return p + 1
                continue
            else:
                print(f"{player['Имя']} успешно сбежал!")
                return
        if action == "выбрать оружие":
            print("Выберите оружие:")
            for weapon in player["Оружия"]:
                print(weapon)
            selected_weapon = input()
            while selected_weapon not in player["Оружия"]:
                print("Неправильный выбор оружия! Выберите одно из доступных:")
                for weapon in player["Оружия"]:
                    print(weapon)
                selected_weapon = input()
            player["Оружие"] = player["Оружия"][selected_weapon]
            print(f"{player['Имя']} выбрал оружие {selected_weapon}")
        elif action == "ударить":
            player_attack = player["Сила"] + random.randint(-2, 2)
            player_damage = random.randint(player["Оружие"]["Атака"][0], player["Оружие"]["Атака"][1])
            enemy_defence = enemy["Защита"] + random.randint(-1, 1)
            damage = max(player_attack - enemy_defence, 0)
            print(f"{player['Имя']} атакует {enemy['наименование врага']} на {damage} урона!")
            time.sleep(2)
            enemy["Здоровье"] -= damage
            if enemy["Здоровье"] <= 0:
                print(f"{player['Имя']} побеждает {enemy['наименование врага']}!")
                time.sleep(2)
                player["Ваши вещи"].append(enemy["наименование врага"])
                win(enemy)
                return
            else:
                enemy_attack = enemy["Сила"] + random.randint(-2, 2)
                player_defence = player["Защита"] + random.randint(-1, 1)
                damage = max(enemy_attack - player_defence, 0)
                print(f"{enemy['наименование врага']} атаковал {player['Имя']} на {damage} урона!")
                time.sleep(2)
                player["Здоровье"] -= damage
                if player["Здоровье"] <= 0:
                    losing()
                    return p + 1

def explore():
    if random.randint(1, 10) <= 3:
        print("Вы исследуете пустошь и ничего не находите.")
    elif random.randint(1, 10) <= 5:
        enemy = random.choice(enemies)
        battle(enemy)
    else:
        new_item()

#Интерфейс
def main():
    while p == 0:
        print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
        time.sleep(0.2)
        print("Выберите действие:")
        time.sleep(0.2)
        print("0. Создать персонажа")
        time.sleep(0.2)
        print("1. Выйти на поиски приключений")
        time.sleep(0.2)
        print("2. Бродячий торговец")
        time.sleep(0.5)
        print("3. Скупщик")
        time.sleep(0.2)
        print("4. Показать статистику игрока")
        time.sleep(0.2)
        print("5. Выйти из игры")
        time.sleep(0.2)
        print("6. Открыть рюкзак")
        time.sleep(0.2)
        print("7. Оружейная лавка")
        choice = input("Введите число (0-6): ")
        print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

        if choice == "0":
            create_player()
        elif choice == "1":
            explore()
        elif choice == "2":
            buy_item()
        elif choice == "3":
            sell_item()
        elif choice == "4":
            show_player_stats()
        elif choice == "5":
            print("Спасибо за игру!")
            break
        elif choice == "6":
            show_items()
        elif choice == "7":
            print("")
            buy_weapon(int(weapon_index))

        else:
            print("Некорректный выбор. Попробуйте еще раз.")
    else:
        create_player()

main()

