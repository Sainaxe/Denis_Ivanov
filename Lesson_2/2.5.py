'''
task 4
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
'''

my_list = [7, 5, 3, 3, 2]
print(f"Rating - {my_list}")
rating = int(input("Enter a number (317 - exit): "))
while rating != 317:
    for el in range(len(my_list)):
        if my_list[el] == rating:
            my_list.insert(el + 1, rating)
            break
        elif my_list[0] < rating:
            my_list.insert(0, rating)
        elif my_list[-1] > rating:
            my_list.append(rating)
        elif my_list[el] > rating and my_list[el + 1] < rating:
            my_list.insert(el + 1, rating)
    print(f"Current list: {my_list}")
    rating = int(input("Enter a number: "))
