'''
task 4
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
'''

task4_str = input("Enter text in line: ")
task4_gram = []
task4_gram = task4_str.split()
print(f"You entered: {task4_gram}, let's split it by elements:")
num = 0
for el in range(task4_str.count(' ') + 1):
    if len(str(task4_gram)) <= 10:
        num += 1
        print(f" {num}: {task4_gram[el]}.")
    else:
        num += 1
        print(f" {num}: {task4_gram[el][0:10]}.")
