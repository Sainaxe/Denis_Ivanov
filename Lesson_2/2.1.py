'''
task1
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''

my_list = [12, 2.34, "str", False, [2, 3]]
print(f"The class of specified list {my_list}: {type(my_list)}.\n"
      f"Class of 1st element: {type(my_list[0])}\n"
      f"Class of 2nd element: {type(my_list[1])}\n"
      f"Class of 3rd element: {type(my_list[2])}\n"
      f"Class of 4th element: {type(my_list[3])}\n"
      f"Class of 5th element: {type(my_list[4])}\n")

# через функцию
my_list = [12, 2.34, "str", False, [2, 3]]


def my_type(i):
    for i in range(len(my_list)):
        print(f"Class of {i + 1}th element: {type(my_list[i])}")
    return


my_type(my_list)
