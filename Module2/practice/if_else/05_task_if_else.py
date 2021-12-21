# Дано целое число m, задающее номер месяца года.
# Выведите строку — название времени года, соответствующего данному месяцу.
# Формат входных данных: дано целое число m (1 ≤ m ≤ 12).
# Формат выходных данных: требуется вывести название времени года

# TODO: your code here

number = int(input("введите номер месяца: "))
if number == 12 or number <= 2:
    print("winter")
elif number > 2 and number <= 5:
    print("spring")
elif number > 5 and number <= 8:
    print("summer")
else:
    print("autumn")
