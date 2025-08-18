num_float = 0

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

num = 3

permit_print = True

if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')

def grade_from_course(course) -> str:
    if course in (1, 2, 3, 4):
        print('Вы бакалавр!')
    elif course in (5, 6):
        print('Вы магистр!')
    elif course in (7, 8, 9):
        print('Вы аспирант!')
    else:
        print('Введите корректный год обучения!')

grade_from_course(3)

some_num = 200

if some_num > 100 or some_num < -100:
    print('-')
else:
    print('+')