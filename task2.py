# Задача 2. Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

# первый вариант решения
lst = ['красный', 'синий', 'белый', 'зе2леный']
num = 2
ans = False
for i in lst:
    for j in i:
        if j == str(num):
            ans = True
            break
print(ans)

# второй вариант решения
lst = ['красный', 'синий', 'белый', 'зе2лёный']
num = 2
ans = False
for i in lst:
    if str(num) in i:
        ans = True
        break
print(ans)

# третий вариант решения
lst = ['красный', 'синий', 'белый', 'зе2лёный']
num = 2
ans = False
for i in lst:
    if i.count(str(num)):
        ans = True
        break
print(ans)