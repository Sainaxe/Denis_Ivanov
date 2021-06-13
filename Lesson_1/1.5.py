'''
task5
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма.
Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки.
Это отношение прибыли к выручке.
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.
'''

revenue = int(input("Enter revenue (EUR): "))
costs = int(input("Enter costs (EUR): "))
if revenue > costs:
    profit = revenue - costs
    print(f"Your result: profit {profit} EUR.")
    rentability = revenue/costs*100
    print(f"Your rentability: {rentability:.1f}%.")
    number_of_employees = int(input("Enter number of employees: "))
    profit_per_employee = revenue/number_of_employees
    net_profit_per_employee = (revenue - costs)/number_of_employees
    print(f"Your profit per employee: {profit_per_employee:.1f} EUR."
          f" Net profit per employee: {net_profit_per_employee:.1f} EUR.")
else:
    loss = costs - revenue
    print(f"Your result: loss {loss} EUR. Come back when you will have a profit!")
print()
