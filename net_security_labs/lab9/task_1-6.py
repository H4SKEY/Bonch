from utils import EllipticCurve, mod_inverse

# Исходные данные варианта 7
p = 37
a = 10
b = 2
G = (23, 35)
N_group = 40
z = 58

print("--- Задание 1-2: Параметры кривой ---")
curve = EllipticCurve(a, b, p)
curve.N = N_group
print(f"Уравнение: y^2 = x^3 + {a}x + {b} mod {p}")
print(f"Точка G на кривой: {curve.is_on_curve(G[0], G[1])}")

print("\n--- Задание 3: Порядок подгруппы и кофактор ---")

n_G = curve.find_order(G)
h = N_group // n_G
print(f"Порядок точки G (n): {n_G}")
print(f"Кофактор (h = N/n): {h}")


curve.order = n_G

print("\n--- Задание 4: Генерация ключей ---")

import random
# закрытый ключ d случайно из [1, n-1]
d = random.randint(1, n_G - 1)
print(f"Закрытый ключ (d): {d}")

Q = curve.multiply_point(d, G)
print(f"Открытый ключ (Q = d*G): {Q}")

print("\n--- Задание 5: Подписание ---")
# Приведение хеша по модулю n
e = z % n_G
print(f"Хеш транзакции z={z}, приведенный по модулю n={n_G}: e={e}")

# Выбор случайного k
k = random.randint(1, n_G - 1)
k = 2 

P_point = curve.multiply_point(k, G)
r = P_point[0] % n_G
if r == 0:
    raise Exception("r=0, выберите другой k")

k_inv = mod_inverse(k, n_G)
s = (k_inv * (e + r * d)) % n_G
if s == 0:
    raise Exception("s=0, выберите другой k")

print(f"Случайное k: {k}")
print(f"Подпись (r, s): ({r}, {s})")

print("\n--- Задание 6: Верификация ---")
w = mod_inverse(s, n_G)
u1 = (e * w) % n_G
u2 = (r * w) % n_G

P_verify = curve.add_points(curve.multiply_point(u1, G), curve.multiply_point(u2, Q))
v = P_verify[0] % n_G

print(f"u1: {u1}, u2: {u2}")
print(f"Точка P': {P_verify}")
print(f"v = x_P' mod n: {v}")
print(f"r: {r}")

if v == r:
    print("РЕЗУЛЬТАТ: Подпись ВЕРНА.")
else:
    print("РЕЗУЛЬТАТ: Подпись НЕВЕРНА.")