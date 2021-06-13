'''
task2
Пользователь вводит время в секундах.
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
'''

s = int(input("Enter time in seconds: "))
c = s
m = s//60
h = m//60
s = s % 60
print(f"You entered: {c} sec., that is equivalent to {h:02}:{m:02}:{s:02} (hh:mm:ss)")
print()
