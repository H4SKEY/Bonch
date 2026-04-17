import hashlib


# Исходные хеши из Задания 3 (SHA3-256)
L1 = "0495d12b38ace51eece0db193b909a1cb5a906274fb36794f3a1e3292905a9ae"
L2 = "7a29a37653b21d7e86bf9de73fb28451a0ed6431b430e6c3ca2f776c626e7d15"
L3 = "8e30335d33acf47657e4c84144cd2f02ed988f4c4e93431f301421012f395ddc"
L4 = L3  # Дублирование последнего элемента

def merkle_parent(h1_hex: str, h2_hex: str) -> str:
    """Вычисляет родительский хеш. Конкатенация бинарных представлений."""
    bin_1 = bytes.fromhex(h1_hex)
    bin_2 = bytes.fromhex(h2_hex)
    combined = bin_1 + bin_2
    return hashlib.sha3_256(combined).hexdigest()

# Расчет узлов
H12 = merkle_parent(L1, L2)
H34 = merkle_parent(L3, L4)
Root = merkle_parent(H12, H34)

print(f"H12: {H12}")
print(f"H34: {H34}")
print(f"Root: {Root}")

