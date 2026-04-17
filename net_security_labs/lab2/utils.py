# Утилиты
import math
from decimal import Decimal, getcontext

# Расширенная точность для float
getcontext().prec = 28

# Вещественная кривая
def is_on_curve_real(x, y, a, b, eps=1e-12):
    """Проверка принадлежности точки вещественной кривой y^2 = x^3 + a*x + b"""
    lhs = y * y
    rhs = x * x * x + a * x + b
    return abs(lhs - rhs) < eps

def point_add_real(P, Q, a, b):
    """Сложение двух точек на вещественной кривой (возвращает None для бесконечной точки)"""
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and y1 == y2:
        # удвоение
        if abs(y1) < 1e-12:
            return None
        s = (3 * x1 * x1 + a) / (2 * y1)
    else:
        if abs(x1 - x2) < 1e-12:
            return None
        s = (y1 - y2) / (x1 - x2)
    x3 = s * s - x1 - x2
    y3 = s * (x1 - x3) - y1
    return (x3, y3)

def scalar_mult_real(k, P, a, b):
    """Скалярное умножение (алгоритм удвоения-сложения) для вещественной кривой"""
    result = None
    addend = P
    while k > 0:
        if k & 1:
            result = point_add_real(result, addend, a, b)
        addend = point_add_real(addend, addend, a, b)
        k >>= 1
    return result

# Кривая над полем GF(p)
def modinv(x, p):
    """Обратный элемент по модулю p (расширенный алгоритм Евклида)"""
    return pow(x, -1, p)

def point_add_mod(P, Q, a, b, p):
    """Сложение двух точек на кривой над GF(p)"""
    if P is None:
        return Q
    if Q is None:
        return P
    x1, y1 = P
    x2, y2 = Q
    if x1 == x2 and y1 == y2:
        # удвоение
        if y1 == 0:
            return None
        s = (3 * x1 * x1 + a) * modinv(2 * y1, p) % p
    else:
        if x1 == x2:
            return None
        s = (y1 - y2) * modinv(x1 - x2, p) % p
    x3 = (s * s - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p
    return (x3, y3)

def scalar_mult_mod(k, P, a, b, p):
    """Скалярное умножение для кривой над GF(p)"""
    result = None
    addend = P
    while k > 0:
        if k & 1:
            result = point_add_mod(result, addend, a, b, p)
        addend = point_add_mod(addend, addend, a, b, p)
        k >>= 1
    return result