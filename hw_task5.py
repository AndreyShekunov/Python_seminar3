# Задание 5. Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Например:
#     - для k = 8 список будет выглядеть так:
#     [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# функция Фибоначчи
def fibo(n):
    if n == 0 or n == 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

# функция создания и заполнения списка Негафибоначчи
def negafib(n):
    lst = []
    for i in range(1, n + 1):
        lst.append(fibo(i)) 
        lst.insert(0, 0)
    for i in range(1, n + 1):
        lst.insert(0, (-1) ** (i + 1) * fibo(i))
    return lst

n = int(input('Введите число: '))
print(negafib(n))
