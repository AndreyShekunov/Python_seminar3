# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Например:
#     - 45 -> 101101
#     - 3 -> 11
#     - 2 -> 10

def print_binary_view(number):
    if number <= 0:
        return
    else:
       print_binary_view(number // 2)
       print(number % 2, end='')

num = int(input('Введите число: '))
print_binary_view(num)