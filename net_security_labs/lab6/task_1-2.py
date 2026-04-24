from utils import generate_shares

# Исходные данные 
p = 53
M = 31
a1 = 5
a2 = 3
n = 5  # Количество участников

print(f"--- Задание 2 ---")
print(f"Параметры: p={p}, M={M}, a1={a1}, a2={a2}")
print(f"Полином: F(x) = {M} + {a1}x + {a2}x^2 mod {p}")

# Коэффициенты для генерации [a1, a2]
coeffs = [a1, a2]

shares = generate_shares(p, M, coeffs, n)

print("\nРаспределенные доли (x, y):")
for share in shares:
    print(f"Участник {share[0]}: {share}")