from utils import create_transaction_string, get_hash_sha3_256, get_hash_sha1

# Данные транзакций
t1 = {
    "txn_id": "tx-001-credit",
    "timestamp": "2026-04-18T10:00:00",
    "borrower_id": "1234567890",
    "lender_id": "SBERBANK",
    "amount": "500000",
    "currency": "RUB",
    "term_months": "24",
    "status": "issued"
}

t2 = {
    "txn_id": "tx-002-credit",
    "timestamp": "2026-04-18T11:30:00",
    "borrower_id": "0987654321",
    "lender_id": "VTBBANK",
    "amount": "1500000",
    "currency": "RUB",
    "term_months": "60",
    "status": "issued"
}

t3 = {
    "txn_id": "tx-003-credit",
    "timestamp": "2026-04-18T12:15:00",
    "borrower_id": "1234567890",
    "lender_id": "SBERBANK",
    "amount": "500000",
    "currency": "RUB",
    "term_months": "24",
    "status": "paid"
}

transactions = [t1, t2, t3]

print("=== Задание 3: Хеширование SHA3-256 ===")
hashes_sha3 = []
for i, txn in enumerate(transactions, 1):
    txn_str = create_transaction_string(txn)
    h = get_hash_sha3_256(txn_str)
    hashes_sha3.append(h)
    print(f"T{i} Hash (SHA3-256): {h}")

print("\n=== Задание 4: Хеширование SHA1 ===")
hashes_sha1 = []
for i, txn in enumerate(transactions, 1):
    txn_str = create_transaction_string(txn)
    h = get_hash_sha1(txn_str)
    hashes_sha1.append(h)
    print(f"T{i} Hash (SHA1): {h}")

print("\n=== Сравнение результатов ===")
print("Длина хеша SHA3-256: 64 символа (256 бит)")
print("Длина хеша SHA1: 40 символов (160 бит)")
print("Значения хешей полностью отличаются из-за разных алгоритмов.")