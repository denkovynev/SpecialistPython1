# Даны два целых числа.
# Вывести список всех чисел кратных трем в диапазоне между заданными числами.

first_number = int(input())     # Первое число
second_number = int(input())    # Второе число

# TODO: your code here
digits = [first_number, second_number]
max_number = max(digits)
min_number = min(digits)
list = []
# TODO: your code here
while min_number <= max_number:
    if min_number % 3 == 0:
       list.append(min_number)
    min_number += 1
print(list)
