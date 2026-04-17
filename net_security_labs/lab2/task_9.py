# Задание 9
from utils import point_add_mod

# Исходные данные
p = 41
a = 11
b = 20
P2 = (20, 9)
Q2 = (10, 33)

print("=== Задание 9 ===")
R = point_add_mod(P2, Q2, a, b, p)
print(f"R = P2 + Q2 = ({R[0]}, {R[1]})")

# Проверка принадлежности
lhs = (R[1] * R[1]) % p
rhs = (R[0]**3 + a*R[0] + b) % p
on = (lhs == rhs)
print(f"Точка R {'принадлежит' if on else 'НЕ принадлежит'} кривой")