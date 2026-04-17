# Задание 10
from utils import point_add_mod

# Исходные данные
p = 41
a = 11
b = 20
P2 = (20, 9)

print("=== Задание 10 ===")
R = point_add_mod(P2, P2, a, b, p)  # удвоение
print(f"2P2 = ({R[0]}, {R[1]})")

# Проверка принадлежности
lhs = (R[1] * R[1]) % p
rhs = (R[0]**3 + a*R[0] + b) % p
on = (lhs == rhs)
print(f"Точка 2P2 {'принадлежит' if on else 'НЕ принадлежит'} кривой")