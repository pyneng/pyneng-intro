"""
Запросить у пользователя ввод индекса (числа) через input. Если по введенному
индексу можно вывести слово из списка words, вывести его. Если индекс больше
допустимого, вывести сообщение "В списке words нет такого индекса".

Пример работы задания
$ python task_07.py
Введите индекс: 0
word1

$ python task_07.py
Введите индекс: 2
word3

$ python task_07.py
Введите индекс: 5
В списке words нет такого индекса

Задание можно усложить добавив поддержку отрицательных индексов:

$ python task_07.py
Введите индекс: -1
word3

$ python task_07.py
Введите индекс: -3
word1

$ python task_07.py
Введите индекс: -4
В списке words нет такого индекса
"""
words = ["word1", "word2", "word3"]
index = int(input("Введите индекс числа: "))
index_max = len(words) - 1
index_min = 0 - len(words)

if index <= index_max and index >= index_min:
    print(words[index])
else:
    print("В списке words нет такого индекса")
