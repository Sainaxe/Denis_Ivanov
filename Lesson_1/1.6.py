'''
task6
Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
'''

a = float(input("Enter fist result of your run (km): "))
b = float(input("Enter target run result (km): "))
if a < 0 or b < 0:
    print("For calculation you need to use positive numbers!")
elif a > b:
    print("Congratulations! You already done target run result.")
else:
    d = 1
    while a < b:
        a += a * 0.1
        d += 1
        print(f"Day {d-1} results will be: {a:.1f} km;")
    print(f"Target run result will be achieved in {d-1} days.")
