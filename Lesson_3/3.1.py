'''
task1
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''

# x, y = (int(input("Enter x, y (numerator / denominator): ")) for _ in range (2))
# x, y = (int(input()) for _ in range(2))
x, y = (int(i) for i in input("Enter x, y (numerator / denominator): ").split())
if y != 0:
    def arg(x, y):
        z = x / y
        return z
    print(f"The result of dividing the x / y: {x / y}")
else:
    print("Cannot be divided by 0")
