# Дано целое число.
# Если оно делится на 3 без остатка - вывести "Foo",
# если делится на 5 - вывести "Bar",
# а если делится на 3 и на 5 - вывести "Foobar".
# Для всех остальных случаев не выводить ничего.

# TODO: your code here
number = int(input("введите число: "))
if number % 3 == 0 and number % 5 == 0:
    print("FooBar")
elif number % 5 == 0:
    print("Bar")
elif number % 3 == 0:
    print("Foo")
