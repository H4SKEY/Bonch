# Задание 6
from utils import is_on_curve_real, scalar_mult_real
from decimal import Decimal

# Исходные данные
a = 11
b = 20
n = 225
P1 = (Decimal('2.5'), Decimal('7.94512'))

print("=== Задание 6 ===")
R = scalar_mult_real(n, P1, a, b)
print(f"{n}·P1 = ({R[0]:.12f}, {R[1]:.12f})")

on = is_on_curve_real(R[0], R[1], a, b)
print(f"Точка {n}·P1 {'принадлежит' if on else 'НЕ принадлежит'} кривой")