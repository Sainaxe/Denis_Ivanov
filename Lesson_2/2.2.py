'''
task2
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
'''

t2_list = list(input("Enter the list elements in line (without no spaces, commas, etc.): "))
j = 0
for i in range(int(len(t2_list) / 2)):
    t2_list[j], t2_list[j + 1] = t2_list[j + 1], t2_list[j]
    j += 2
print(t2_list)
# не смог довести до ума: как ограничить элемент пробелами (для возможности введения многознака) и потом убрать пробелы

# решение через последователный ввод (возможность принимать на ввод списка элементы более 1-го знака)
t2_list_1 = int(input("Enter the TOTAL number of list elements: "))
my_list = []
i = 0
el = 0
while i < t2_list_1:
    my_list.append(input(f"Enter the {i + 1}th element: "))
    i += 1
for el in range(int(len(my_list) / 2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print(my_list)
