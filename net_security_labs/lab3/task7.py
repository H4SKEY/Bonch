import hashlib

def merkle_parent(h1_hex: str, h2_hex: str) -> str:
    """Вычисляет родительский хеш. Конкатенация бинарных представлений."""
    bin_1 = bytes.fromhex(h1_hex)
    bin_2 = bytes.fromhex(h2_hex)
    combined = bin_1 + bin_2
    return hashlib.sha3_256(combined).hexdigest()

# Данные для проверки
L1 = "0495d12b38ace51eece0db193b909a1cb5a906274fb36794f3a1e3292905a9ae"
L2_proof = "7a29a37653b21d7e86bf9de73fb28451a0ed6431b430e6c3ca2f776c626e7d15"
H34_proof = "be2cff182895f290cc757cab3b602ac675202ce4e22be5b0d3a7d055dcefd980"
Root_expected = "6ccb6fa0795aad8dd3fffabc4fdaf5a6fdf532a7a237f822bec17fe523b13797"

print("=== Задание 7: Верификация доказательства Меркла для T1 ===")

# Шаг 1: H12 из L1 и соседа L2
H12_calc = merkle_parent(L1, L2_proof)
print(f"1. H(L1 + L2): {H12_calc[:10]}...")

# Шаг 2: Root из полученного H12 и соседа H34
Root_calc = merkle_parent(H12_calc, H34_proof)
print(f"2. Root(H12 + H34): {Root_calc[:10]}...")

# Сравнение
if Root_calc == Root_expected:
    print("\nРезультат: УСПЕХ. Доказательство верно. Транзакция T1 принадлежит блоку.")
else:
    print("\nРезультат: ОШИБКА. Хеш корня не совпадает.")