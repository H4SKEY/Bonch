# Задание 3
from utils import is_on_curve_real
from decimal import Decimal

# Исходные данные
a = 11
b = 20
P1 = (Decimal('2.5'), Decimal('7.94512'))
Q1 = (Decimal('0.44646'), Decimal('5'))

def check(name, point):
    x, y = point
    on = is_on_curve_real(x, y, a, b)
    print(f"Точка {name} = ({x}, {y}) -> {'принадлежит' if on else 'НЕ принадлежит'} кривой")

print("=== Задание 3 ===")
check("P1", P1)
check("Q1", Q1)