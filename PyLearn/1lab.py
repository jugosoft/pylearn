"""
1 Создать лист из 6 любых чисел. Отсортировать его по возрастанию
2 Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно
3 Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем
4 Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку, чтобы получилось: 'Earth -> Russia -> Moscow'
5 Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'
6 Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет
7 Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы
8 Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс
9 Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'
10 Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль

Материалы:
tuple vs list: http://stackoverflow.com/questions/1708510/python-list-vs-tuple-when-to-use-each http://stackoverflow.com/questions/626759/whats-the-difference-between-lists-and-tuples http://nedbatchelder.com/blog/201608/lists_vs_tuples.html
dict: https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html
Что такое enumerate? http://pythonz.net/references/named/enumerate/
Как перевернуть коллекцию? https://ru.stackoverflow.com/questions/427051/%D0%A4%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D1%8F-reversed-%D0%B2-%D0%9F%D0%B8%D1%82%D0%BE%D0%BD%D0%B5
Как сортировать? https://wiki.python.org/moin/HowTo/Sorting
Как соединять и разбивать строки? http://www.diveintopython.net/native_data_types/joining_lists.html
Является ли dict упорядоченным? https://stackoverflow.com/questions/1867861/python-dictionary-how-to-keep-keys-values-in-same-order-as-declared
Продвинутые материалы:
Какие еще есть коллекции? https://docs.python.org/2/library/collections.html
Что такое хеш-таблица? https://ru.wikipedia.org/wiki/%D0%A5%D0%B5%D1%88-%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D0%B0
Как python определяет термин "hashable"? https://docs.python.org/3/glossary.html -> hashable
Как считается hash в python? https://stackoverflow.com/questions/14535730/what-do-you-mean-by-hashable-in-python
Могут ли быть коллизии в хеш-таблицах? https://en.wikipedia.org/wiki/Hash_table#Collision_resolution
Видео:
Как устроен современный dict? https://www.youtube.com/watch?v=p33CVV29OG8
"""

#0
separator = '8*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*8'

#1
print(1)
arr = [1, 2, 3, 6, 4, 5]
n = len(arr)
#array.sort()
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1] :
            #true pythonic solution :)
            #arr[j], arr[j + 1] = arr[j + 1], arr[j]
            arr[j]      = arr[j] ^ arr[j + 1]
            arr[j + 1]  = arr[j] ^ arr[j + 1]
            arr[j]      = arr[j] ^ arr[j + 1]
print(arr)
print(separator)

#2
print(2)
d = {1 : '1',
     2 : '2',
     3 : '3',
     4 : '4',
     5 : '5',
     6 : '6'}

for x in d:
    print('key ' + str(x) + ' val ' + d[x])

print(separator)

#3
print(3)
turple = (0.2, 0.228, 0.1488, 0.227, 
          2.1488, 2.28, 2.1488, 2.28, 
          1.488, 14.88)
min = turple[0]; max = turple[0]

for x in turple:
    if x < min:
        min = x

    if x > max:
        max = x

print('max ' + str(max) + ' min ' + str(min))
print(separator)

#4
print(4)
arr = ['Earth', 'Russia', 'Moscow']
string = arr[0] + '->'

for x in range(0, len(arr) - 1):
    string += arr[x + 1]
    if x + 1 < len(arr) - 1:
        string += '->'

print(string)
print(separator)

#5
print(5)
string = '/bin:/usr/bin:/usr/local/bin'
result = ['']
counter = 0

for x in string:
    if x != ':':
        result[counter] += x
    else:
        result.append('')
        counter = counter + 1

for x in result:
    print(x)

print(separator)

#6
print(6)
arr = range(1, 101)

#адыкватное решение 1
#res = range(0, 101, 7)

#адыкватное решение 2
#res = [x for x in range(1, 101) if x % 7 == 0]

#classic solution
res = []
for x in arr:
    if x % 7 == 0:
        res.append(x)

print(res)
print(separator)

#7
print(7)
matrix = [[1,   2,   3],
          [4,   5,   6],
          [7,   8,   9],
          [10, 11, 12]]
 
print('strings')
for col in range(len(matrix)):    
    for string in range(len(matrix[col])):
        print(matrix[col][string], end = ' ')
    print()

print()
print('columns\n')

for string in range(len(matrix[col])):
    for col in range(len(matrix)):
        print(matrix[col][string], end = ' ')
    print()

print()
print(separator)

#8
print(8)
arr = list()

while True:
    ob = input("Input object: ")
    if ob == '':
        break
    else:
        arr.append(ob)

for x in range(len(arr)):
    print("#" + str(x) + " " + str(arr[x]))

print(separator)

#9
print(9)

# variant 1
arr = []
arr.append('to-delete')
arr.append('11334')
arr.append('to-delete')
arr.append('boom!')
arr.append('to-delete')

print(arr)

while arr.count('to-delete') != 0:
    arr.remove('to-delete')
    
print(arr)


print(separator)

#10
print(10)
arr = [x for x in range(1, 11)]
print(arr)

#normal
#arr.reverse()

#tryin' to show of
res = []
n = len(arr)

for x in arr:
    res.append(n + 1 - x)

print(arr)
print(separator)

