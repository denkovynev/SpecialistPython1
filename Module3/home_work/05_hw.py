# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
max_len_names = len(names[0])
max_names = ""
for name in names:
    if len(name) > max_len_names:
        max_len_names = len(name)
        max_names = name
print(max_names)
