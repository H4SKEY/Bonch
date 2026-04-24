def mod_inverse(a, m):
    """Нахождение обратного элемента a по модулю m"""
    if a < 0:
        a = a % m
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError('Обратный элемент не существует')
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

    def is_on_curve(self, x, y):
        if x is None and y is None:
            return True
        return (y * y - (x * x * x + self.a * x + self.b)) % self.p == 0

    def add_points(self, P, Q):
        if P is None: return Q
        if Q is None: return P
        
        x1, y1 = P
        x2, y2 = Q
        
        if x1 == x2 and y1 != y2:
            return None # Точка в бесконечности
        
        if x1 == x2 and y1 == y2:
            # Удвоение точки
            if y1 == 0:
                return None
            lam = (3 * x1 * x1 + self.a) * mod_inverse(2 * y1, self.p) % self.p
        else:
            # Сложение точек
            lam = (y2 - y1) * mod_inverse(x2 - x1, self.p) % self.p
            
        x3 = (lam * lam - x1 - x2) % self.p
        y3 = (lam * (x1 - x3) - y1) % self.p
        return (x3, y3)

    def multiply_point(self, k, P):
        """Скалярное умножение k * P"""
        if k % self.order == 0 or P is None:
            return None
        if k < 0:
            # Отрицательное скалярное умножение: -k * P = k * (-P)
            return self.multiply_point(-k, (P[0], -P[1] % self.p))
        
        result = None
        addend = P
        
        while k:
            if k & 1:
                result = self.add_points(result, addend)
            addend = self.add_points(addend, addend)
            k >>= 1
        return result

    def find_order(self, P):
        """Поиск порядка точки P (методом перебора делителей N или полным перебором для малых N)"""
        if P is None:
            return 1
        current = P
        for i in range(1, self.N + 1):
            if current is None:
                return i
            current = self.add_points(current, P)
        return None # Не найдено в пределах N