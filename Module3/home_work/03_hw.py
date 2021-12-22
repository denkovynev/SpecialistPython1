# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random
n = int(input("Введите n "))
numbers = []
i = 0
summa = 0
while i < n:
    i += 1
    numbers.append(random.randint(-100, 100))
print(numbers)
for k in numbers:
    if k % 2 ==0 and k>0:
        summa = summa + k
print(summa)
