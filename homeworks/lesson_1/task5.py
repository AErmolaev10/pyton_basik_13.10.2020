"""
Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""

revenue = int(input('Введите значение выручки'))
expenses = int(input('Введите издержки фирмы'))

profit = revenue - expenses
profitability = profit / revenue
profitability_print = f'Рентабельность выручки {profitability:0.2f}'

if profit > 0:
    print(profitability_print)
    staff = int(input('Введите количество сотрудников фирмы'))
    profit_staff = profit / staff
    profit_staff_print = f'Прибыль фирмы в расчете на одного сотрудника равна {profit_staff:0.2f}'
    print(profit_staff_print)
else:
    print('У вас нет прибыли')


