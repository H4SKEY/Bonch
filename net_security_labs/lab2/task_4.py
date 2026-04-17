# Задание 4
from utils import is_on_curve_real, point_add_real
from decimal import Decimal

# Исходные данные
a = 11
b = 20
P1 = (Decimal('2.5'), Decimal('7.94512'))
Q1 = (Decimal('0.44646'), Decimal('5'))

print("=== Задание 4 ===")
R = point_add_real(P1, Q1, a, b)
print(f"R = P1 + Q1 = ({R[0]:.12f}, {R[1]:.12f})")

on = is_on_curve_real(R[0], R[1], a, b)
print(f"Точка R {'принадлежит' if on else 'НЕ принадлежит'} кривой")