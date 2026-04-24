def extended_gcd(a, b):
    """
    Расширенный алгоритм Евклида.
    Возвращает (gcd, x, y) такие что a*x + b*y = gcd
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    """
    Нахождение обратного элемента a по модулю m.
    a^-1 mod m
    """
    gcd, x, _ = extended_gcd(a % m, m)
    if gcd != 1:
        raise Exception('Обратный элемент не существует')
    else:
        return x % m

def mod_pow(base, exp, mod):
    """
    Быстрое возведение в степень по модулю (binary exponentiation).
    """
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result