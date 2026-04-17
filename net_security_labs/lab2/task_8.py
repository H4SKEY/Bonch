# Задание 8

# Исходные данные
p = 41
a = 11
b = 20
P2 = (20, 9)
Q2 = (10, 33)

def is_on_curve_mod(x, y, a, b, p):
    lhs = (y * y) % p
    rhs = (x * x * x + a * x + b) % p
    return lhs == rhs

def check_mod(name, point):
    x, y = point
    on = is_on_curve_mod(x, y, a, b, p)
    print(f"Точка {name} = ({x}, {y}) -> {'принадлежит' if on else 'НЕ принадлежит'} кривой")

print("=== Задание 8 ===")
check_mod("P2", P2)
check_mod("Q2", Q2)