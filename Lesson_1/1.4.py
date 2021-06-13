'''
task4
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''

e = int(input("Enter a number (to find the largest digit in a number): "))
rce = e
max_e = e % 10
e = e//10
while e > 0:
    if max_e < e % 10:
        max_e = e % 10
    e = e//10
print(f"You entered: {rce}. The largest digit in a number is {max_e}.")
print()
