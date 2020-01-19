# комментарий
""" комментарий
    но длинее
"""

# https://docs.python.org/3.8/tutorial/index.html

# числа
#

my_number = 93

print('---------------')
print(my_number)  # напечатаем его
print(my_number / 7)  # поделим на 10 и вернет float
print(my_number // 7)  # вернет только целую часть
print(my_number % 7)  # вернет остаток от деления
print(my_number**2)  # возведем в степень 2

print(type(my_number).__name__, my_number.__class__)  # покажет тип переменной

# стринга (строка)
#

my_string = 'string1'
my_string1 = "string2"
long_string = """LONG ONE
LONGER
LONGER
"""
print('---------------')
print(my_string)
print(my_string1)
print(long_string)

# спецсимволы
# https://docs.python.org/2.0/ref/strings.html
print('hello \n polly')
print('hello \t polly')
print("hello \0 polly")  # https://stackoverflow.com/questions/14461695/what-does-0-stand-for/14461711
                         # и в пайтоне себя так не ведет, хоть он и написан на С

print('It\'s another bottle of wine')

# списки (list) или массивы
#

my_list = [1, 2, 3, 4, 5, 6]
my_list2 = ['a', 'b', 'c', 'd']

print('---------------')
print(my_list)
print(my_list2)

print(my_list[0])  # первый элемент
print(my_list2[-1])  # последний элемент
print(len(my_list2))  # длина списка


# dict

print('---------------')
my_dict = {'a': 1, 'b': 2}
print(my_dict)

# set
print('---------------')
my_set = ('a', 21, 'for')
print(my_set)

# Функции


def beta():
    ret = 'function return value'
    print('beta')
    return ret


r = beta()
print(r)

f = open('surnames.txt')
for line in f.readlines():
    print(line.strip())