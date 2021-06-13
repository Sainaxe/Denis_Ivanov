'''
task 3
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
'''

s_list = ['Winter', 'Spring', 'Summer', 'Autumn']
s_dict = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Autumn'}
m = int(input("Enter the month (by use a numbers from 1 to 12):"))
if m == 1 or m == 12 or m == 2:
    print(f"Dict: {s_dict.get(1)}")
    print(f"List: {s_list[0]}")
elif m == 3 or m == 4 or m == 5:
    print(f"Dict: {s_dict.get(2)}")
    print(f"List: {s_list[1]}")
elif m == 6 or m == 7 or m == 8:
    print(f"Dict: {s_dict.get(3)}")
    print(f"List: {s_list[2]}")
elif m == 9 or m == 10 or m == 11:
    print(f"Dict: {s_dict.get(4)}")
    print(f"List: {s_list[3]}")
else:
    print("There is no such month, please enter the correct number!")
