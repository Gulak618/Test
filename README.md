# Игра в города.

Реализована простая игра в города на языке Python, с элементарным искусственным интеллектом для хода компьютера и проверки условий выигрыша или проигрыша.

## Правила игры:
- Игра начинается с того, что компьютер выбирает случайный город из общего списка городов и выводит его на экран;
- Игрок имеет 5 попыток на всю игру, каждый раз, когда игрок называет неверный город, у него снимается 1 попытка. Когда количество попыток будет 0 - игрок проиграл;
- Если компьютер(ИИ) не смог найти город, в ответ на город игрока, то компьютер проиграл;
- Если текущий город оканчивается на какую-то из букв "ь", "ъ", "ы", то игрок/компьютер должен подобрать город, который начинается на первую букву текущего города;
- Перед кажым ходом производится проверка, остались ли в списке города, заканчивающиеся на заданную букву. Если нет, то игрок/компьютер должен подобрать город, который начинается на первую букву текущего города;
