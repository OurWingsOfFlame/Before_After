# Demo-Prototype
import random


class User:
    points = 0
    login = 'Данил'
    ready_task = [100]  # Потом этот пункт надо перенести в класс игры, поскольку пройденные вопросы одинаковы для всех
    # игроков сессии


Danil = User()
Dasha = User()
card1, card2 = 100, 100  # Потом изменить, сейчас 100, потому что вопросов мало и сотого вопроса точно нет. Не знаю,
# как иначе инициализировать, чтобы дальше в основном цикле вытянуть первую карточку
tasks = [['Начало княжения Рюрика', 862], ['Крещение Руси', 988], ['Февральская революция', 1917],
         ['Смерть Сталина', 1953], ['Начало ВОВ', 1941], ['Первое упоминание о Москве', 1147],
         ['Избрание на царство Михаила Федоровича Романова', 1613], ['Основание Санкт-Петербурга', 1703],
         ['Восстание декабристов', 1825], ['Отмена крепостного права', 1861],
         ['Вступление России в первую мировую войну', 1914], ['Образование СССР', 1922],
         ['Полет Ю.А. Гагарина в космос', 1961], ['Распад СССР', 1991], ['Падение Западной Римской империи', 476],
         ['Образование государства франков', 486], ['Возникновение государства остготов в Италии', 493],
         ['Образование Арабского государства', 630], ['Захват кретсоносцами Константинополя', 1204],
         ['Великая хартия вольностей', 1215], ['Первый английский парламент', 1265],
         ['Первые генеральные штаты во Франции', 1302], ['Начало столетней войны', 1337]]
result = 0
flag = False  # Если кто-то набирает 15 очков, обратим флаг в тру
while not flag:  # Основной цикл игры
    while card1 in Danil.ready_task:
        card1 = random.randrange(len(tasks))
    while card2 in Danil.ready_task or card2 == card1:
        card2 = random.randrange(len(tasks))
    print(tasks[card1][0], tasks[card2][0])
    Danil.ready_task.append(card1)
    Danil.ready_task.append(card2)
    if tasks[card1][1] < tasks[card2][1]:
        right_answer = 1
    else:
        right_answer = 2
    danil = int(input('Данил: '))
    dasha = int(input('Даша: '))
    if danil == right_answer and dasha == right_answer:
        Danil.points += 1
        Dasha.points += 1
        if Danil.points == 15 and Dasha.points == 15:
            result = 'Ничья'
            flag = True
        elif Dasha.points == 15:
            result = 'Dasha'
            flag = True
        elif Danil.points == 15:
            result = 'Danil'
            flag = True
    elif dasha == right_answer:
        Dasha.points += 2
        if Dasha.points >= 15:
            result = 'Dasha'
            flag = True
    elif danil == right_answer:
        Danil.points += 2
        if Danil.points >= 15:
            result = 'Danil'
            flag = True
print(result)







