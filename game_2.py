            #рулетка
import random

import termcolor
print(termcolor.colored('*' * 32, 'red'))
print(termcolor.colored('Добро пожаловать и приятной игры!', 'red'))
print(termcolor.colored('*' * 32, 'red'))


money = 10000
bank_casino = 1000000
bank = 0
credit = 0

a = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
b = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
z = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

black = random.choice(a)
red = random.choice(b)
zero = random.choice(z)

wheel = {'красный': red, 'черный': black, 'зеленый': zero}
def credit_money():
    valid = True
    global bank_casino

    global money
    global credit
    while valid:
        try:
            credit = int(input(termcolor.colored('Введите ставку: ','green')))
        except:
            print('Неккоректный ввод. Введите цифру')
            continue
        if credit < 500:
            print('Минимальная ставка 500')
            continue
        if (money - credit) < 0:
            print(f'Ваш баланс меньше нуля {money}')
            continue

        money -= credit

        print(termcolor.colored(f'Ваш баланс {money} у.е.','cyan' ))
        print(termcolor.colored(f'Ваша ставка {credit} у.е.', 'cyan'))


        valid= False




def whell_boart():
    global red
    global black
    global zero
    global wheel
    r = True
    while r:
        x = random.randint(0,37)
        if x % 2 == 0:
            y = wheel['красный']
            print(f'{y} красный')
        elif x % 7 == 0 or x == 0:
            y = wheel['зеленый']
            print(f'{y} зеленый')
        else:
            y = wheel['черный']
            print(f'{y} черный')
        r = False

# whell_boart()


def chek_win():

    global bank_casino
    global bank
    global money
    global credit
    global red
    global black
    global zero
    global wheel
    global a
    global b

    credit_money()
    wow = True
    while wow:
        print('''\r 1. Ставка на один номер
              \r 2. Ставка на два номера
              \r 3. Ставка на три номера
              \r 4. Ставка на цвет
              \r 5. Четный/Нечетный
              \r 6. Ставка на колону''')
        try:
            i = int(input('Выберите тип ставки: '))
        except:
            print('Неккоректный ввод. Введите цифру')
            continue

        if i == 1:
            print('Ставка на один номер')
            try:
                o = int(input('Введите номер от 0 до 36: '))
            except:
                print('Неккоректный ввод.')
                continue
            if o > 36:
                print('\tНомер не должен быть больше 36')
                continue
            whell_boart()
            if o == red or o == black or o == zero:

                bank += credit*35
                bank_casino -= bank
                print(f'Ваш выигрыш {bank}')
            else:
                bank_casino += credit
                print(f'Ваш выигрыш {bank}')
                print(f'В казино осталось {bank_casino}')
                print('ставка проиграла')

        elif i == 2:
            print('Ставка на два номера')
            try:
                f = int(input('Введите номер от 0 до 36: '))
                t = int(input('Введите номер от 0 до 36: '))
            except:
                print('Неккоректный ввод.')
                continue
            if f > 36 or t > 36:
                print('\tНомер не должен быть больше 36')
                continue

            if f != t:
                whell_boart()
                if f == red or f == black or f == zero:

                    bank += credit*17
                    bank_casino -= bank
                    print(f'Ваш выигрыш {bank}')
                elif t == red or t == black or t == zero:
                    bank += credit*17
                    bank_casino -= bank
                    print(f'Ваш выигрыш {bank}')
                else:
                    bank_casino += credit
                    print(f'Ваш выигрыш {bank}')
                    print(f'В казино осталось {bank_casino}')
                    print('ставка проиграла')

            else:
                print('номера не должны совпадать')
                continue

        elif i == 3:
            print('Ставка на три номера')
            try:
                q = int(input('Введите номер от 0 до 36: '))
                w = int(input('Введите номер от 0 до 36: '))
                e = int(input('Введите номер от 0 до 36: '))
            except:
                print('Неккоректный ввод.')
                continue
            if q > 36 or w > 36 or e > 36:
                print('\tНомер не должен быть больше 36')
                continue

            if q != w and w != e and q != e:
                whell_boart()
                if q == red or q == black or q == zero:

                    bank += credit*11
                    bank_casino -= bank
                    print(f'Ваш выигрыш {bank}')
                elif w == red or w == black or w == zero:
                    bank += credit*11
                    bank_casino -= bank
                    print(f'Ваш выигрыш {bank}')
                elif e == red or e == black or e == zero:
                    bank += credit*11
                    bank_casino -= bank
                    print(f'Ваш выигрыш {bank}')
                else:
                    bank_casino += credit
                    print(f'Ваш выигрыш {bank}')
                    print(f'В казино осталось {bank_casino}')
                    print('ставка проиграла')
            else:
                print('номера не должны совпадать')
                continue

        elif i == 4:
            print('Ставка на цвет')
            color = input('Выберите цвет 1-красный, 2-черный: ')
            c = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36, 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
            some = random.choice(c)
            whell_boart()

            if color == '1':
                print('Ставка на красный')
                if some in b:
                    bank += credit
                    bank_casino -= bank
                    print(f'Ваш выигрыш {bank}')
                else:
                    bank_casino += credit
                    print(f'Ваш выигрыш общий {bank}')
                    print(f'В казино осталось {bank_casino}')
                    print('ставка проиграла')
            elif color == '2':
                print('Ставка на черный')
                if some in a:
                    bank += credit
                    bank_casino -= bank
                    print(f'Ваш выигрыш {bank}')
                else:
                    bank_casino += credit
                    print(f'Ваш выигрыш общий {bank}')
                    print(f'В казино осталось {bank_casino}')
                    print('ставка проиграла')


        elif i == 5:
            print('Четное/Нечетное')
            val = input('Выберите 1-Нечетное 2-Четное: ')
            whell_boart()
            if val == '1':
                print('Ставка на нечетное')
                if red % 2 != 0 or black % 2 != 0:
                    bank += credit
                    bank_casino -= bank
                    print(f'Ваш выигрыш {bank}')
                else:
                    bank_casino += credit
                    print(f'Ваш выигрыш {bank}')
                    print(f'В казино осталось {bank_casino}')
                    print('ставка проиграла')
            elif val == '2':
                print('Ставка на четное')
                if red % 2 == 0 or black % 2 == 0:
                    bank += credit
                    bank_casino -= bank
                    print(f'Ваш выигрыш {bank}')
                else:
                    bank_casino += credit
                    print(f'Ваш выигрыш {bank}')
                    print(f'В казино осталось {bank_casino}')
                    print('ставка проиграла')

        elif i == 6:
            print('Ставка на колонну')
            first = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
            second = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
            third = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

            tre = input('Выберите номер колоны 1-3: ')
            whell_boart()
            if tre == '1':
                print('Первая колона')
                if red in first or black in first:
                    bank += credit*2
                    bank_casino -= bank
                    print(f'Ваш выигрыш {bank}')
                else:
                    bank_casino += credit
                    print(f'Ваш выигрыш {bank}')
                    print(f'В казино осталось {bank_casino}')
                    print('ставка проиграла')
            elif tre == '2':
                print('Вторая колона')
                if red in second or black in second:
                    bank += credit*2
                    bank_casino -= bank
                    print(f'Ваш выигрыш {bank}')
                else:
                    bank_casino += credit
                    print(f'Ваш выигрыш {bank}')
                    print(f'В казино осталось {bank_casino}')
                    print('ставка проиграла')
            elif tre == '3':
                print('Третья колона')
                if red in third or black in third:
                    bank += credit*2
                    bank_casino -= bank
                    print(f'Ваш выигрыш {bank}')
                else:
                    bank_casino += credit
                    print(f'Ваш выигрыш {bank}')
                    print(f'В казино осталось {bank_casino}')
                    print('ставка проиграла')
        wow = False
chek_win()
cont = True
while cont:
    ul = input(termcolor.colored('Продолжить игру? Нажмите y/n: ', 'magenta'))
    if ul == 'y':

        chek_win()
    elif ul == 'n':
        money += bank
        print(termcolor.colored(f'Ваш выигрыш {bank} у.е.', 'green'))
        print(termcolor.colored(f'В казино осталось {bank_casino} у.е.', 'green'))
        print(termcolor.colored(f'Ваш баланс составляет: {money} у.е.', 'green'))
        cont = False

