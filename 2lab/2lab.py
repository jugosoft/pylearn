# Задачи на закрепление типов аргументов:
# Написать функцию, которая принимает любое количество аргументов чисел.
# Среди них она находит максимальное и минимальное. И возвращает оба
print('Домашнее задание. День 3. Типы аргументов. Задание 1\n')
def extremum_func(*numbers):
    min = numbers[0]; max = numbers[0]
    for x in numbers:
        if x > max:
            max = x
        if x < min:
            min = x
    return min, max

results = extremum_func(1.25, 2, 5, 1.2, 23, 5, 2, 5, 7, 2, 6, 5, 7, 2, 666, 5, 73, 22, 16)
print("minimal number is " + str(results[0]) + ", but max is " + str(results[1]))

# Написать функцию, которая принимает два аргумента: строка и булевый флаг case по-умолчанию равный True.
# Если флаг действителен: возвращаем новую строку, где каждый символ входной приведен к верхнему регистру, иначе - к нижнему
print('\n\nДомашнее задание. День 3. Типы аргументов. Задание 2\n')
def case_switcher(string : str, flag : bool):
    if flag:
        return string.upper()
    return string.lower()

print(case_switcher('I\'m your father Luke!',True))

# Написать функцию, которая принимает любое количество позиционных аргументов - строк
# и один парматер по-умолчанию glue, который равен ':'.
# Соединить все строки таким образом, чтобы в результат попали все строки, длинее 3 символов.
# Для соединения между любых двух строк вставлять glue
print('\n\nДомашнее задание. День 3. Типы аргументов. Задание 3\n')
def smart_concat(*text, glue=':'):
    string = ''

    for x in text:
        if len(x) > 3:
            string += x + glue
    length = len(string) - 1

    if string[length] == ':':
        l = list(string)
        del l[length]
        string = "".join(l)
    return string

print(smart_concat('123', '2234', '11111111', '33', '666', '7777'))