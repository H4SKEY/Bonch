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

def mod_inverse(a, p):
    """
    Нахождение обратного элемента a по модулю p.
    a^-1 mod p
    """
    gcd, x, _ = extended_gcd(a % p, p)
    if gcd != 1:
        raise Exception('Обратный элемент не существует')
    else:
        return x % p

def lagrange_interpolation_secret(shares, p):
    """
    Восстановление секрета (свободного члена полинома) по схеме Шамира
    используя интерполяцию Лагранжа в точке x=0.
    
    shares: список кортежей (x, y)
    p: простое число (модуль поля)
    """
    k = len(shares)
    secret = 0
    
    for j in range(k):
        x_j, y_j = shares[j]
        numerator = 1
        denominator = 1
        
        for m in range(k):
            if m == j:
                continue
            x_m, _ = shares[m]

            numerator = (numerator * (0 - x_m)) % p
            denominator = (denominator * (x_j - x_m)) % p
            
        denom_inv = mod_inverse(denominator, p)
        
        term = (y_j * numerator * denom_inv) % p
        secret = (secret + term) % p
        
    return secret

def generate_shares(p, M, coeffs, n):
    """
    Генерация долей секрета.
    p: модуль
    M: секрет (a0)
    coeffs: список коэффициентов [a1, a2, ...]
    n: количество долей
    """
    shares = []
    all_coeffs = [M] + coeffs
    
    for i in range(1, n + 1):
        y = 0
        for power, coeff in enumerate(all_coeffs):
            y = (y + coeff * pow(i, power, p)) % p
        shares.append((i, y))
        
    return shares