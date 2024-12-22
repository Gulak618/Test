from random import choice
import sys


f = open("cities.txt")
cities_list = [line.strip() for line in f]
f.close()

f = open("answers.txt", "w")

counter = 0
first_move = choice(cities_list)


def computer_move(cities_list, prev_move):
    char = prev_move[-1]
    available_moves = []
    for word in cities_list:
        if word[0].lower() == char:
            available_moves.append(word)
    if any(available_moves):
        move = choice(available_moves)
        prev_move = move
        cities_list.remove(move)
        f.write(move + "\n")
        print(f"Ход компьютера: {move}")
        return move
    else:
        print(f"Не было найдено городов на {char} - поиск на {prev_move[0].lower()}")
        char = prev_move[0].lower()
        for word in cities_list:
            if word[0].lower() == char:
                available_moves.append(word)
        if any(available_moves):
            move = choice(available_moves)
            prev_move = move
            cities_list.remove(move)
            f.write(move + "\n")
            print(f"Ход компьютера: {move}")
            return move
        else:
            print(f"Не было найдено городов на {char} - компьютер проиграл!")
            f.close()
            sys.exit()


def user_move(cities_list, user_imp, prev_move, counter):
    city = user_imp
    for word in cities_list:
        if word[0].lower() == prev_move[-1].lower():
            break
    else:
        print(f"Городов на {prev_move[-1]} не осталось - введите город на {prev_move[0].lower()}")
        prev_move = prev_move[::-1].lower()
        return [0, prev_move, counter]
    for word in cities_list:
        if word.lower() == city.lower():
            break
    else:
        counter += 1
        if counter == 5:
            print("5 неудачных попыток ввода. Вы проиграли!")
            sys.exit()
        print(f"Такого города нет, или он уже был назван! Повторите попытку. Осталось попыток: {5 - counter}")
        return [False, prev_move, counter]
    if city[0].lower() == prev_move[-1].lower():
        cities_list.remove(city)
        prev_move = city
        f.write(city + "\n")
        return [True, prev_move, counter]


print("___Игра в города___")
print(f"Первый ход компьютера: {first_move}")
cities_list.remove(first_move)
f.write(first_move + "\n")
prev_move = [0, first_move, counter]
while True:
    usr_move = user_move(cities_list, input("Ваш ход: "), prev_move[1], prev_move[2])
    prev_move = usr_move.copy()
    if not usr_move[0]:
        continue
    prev_move[1] = computer_move(cities_list, prev_move[1])