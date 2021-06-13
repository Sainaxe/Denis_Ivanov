'''
task3
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

n = int(input("Enter an integer to calculate the expression: "))
q = n
nn = n*10+q
nnn = nn*10+q
w = q+nn+nnn
print(f"You entered {q}: {q}+{nn}+{nnn}={w}")
print()
