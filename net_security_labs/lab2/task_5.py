# Задание 5
from utils import is_on_curve_real, point_add_real
from decimal import Decimal

# Исходные данные
a = 11
b = 20
P1 = (Decimal('2.5'), Decimal('7.94512'))

print("=== Задание 5 ===")
R = point_add_real(P1, P1, a, b)  # удвоение
print(f"2P1 = ({R[0]:.12f}, {R[1]:.12f})")

on = is_on_curve_real(R[0], R[1], a, b)
print(f"Точка 2P1 {'принадлежит' if on else 'НЕ принадлежит'} кривой")