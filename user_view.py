from Task_1 import *
from Task_2 import *
from Task_3 import *
import math
def user_menu():
    menu = '*** Задача №1 ***\n' \
           ' *** Задача №2 ***\n' \
           ' *** Задача №3 ***\n' \
           ' Чтобы закончить введите "end"\n' \
           '------------------------------'
    user = input((f'Привет! Что будем проверять на этот раз?\n {menu} \n'))
    while user.lower() != 'end':
        if user.lower() == 'задача №1' or user.lower() == 'задача 1' or user.lower() == '1':
            num = float(input('Введите точность d: '))
            number(num)
            user = input((f'\nЧто будем проверять дальше?\n {menu} \n'))
        elif user.lower() == 'задача №2' or user.lower() == 'задача 2' or user.lower() == '2':
            number_task_2 = int(input('Введите натурально число:'))
            print(just_mn(number_task_2))
            user = input((f'\nЧто будем проверять дальше?\n {menu} \n'))
        elif user.lower() == 'задача №3' or user.lower() == 'задача 3' or user.lower() == '3':
            win = {}
            nich = {}
            poraj = {}
            commands = []
            matches(poraj, win, nich, commands)
            ochki(poraj, win, nich, commands)
            user = input((f'\nЧто будем проверять дальше?\n {menu} \n'))
        else:
            print('Я тебя не понимаю. Давай ещё раз')
            user = input((f'Что будем проверять?\n {menu} \n'))