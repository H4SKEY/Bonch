import hashlib
import json

def get_hash_sha3_256(data_str: str) -> str:
    """Вычисляет хеш SHA3-256 для входной строки"""
    return hashlib.sha3_256(data_str.encode('utf-8')).hexdigest()

def get_hash_sha1(data_str: str) -> str:
    """Вычисляет хеш SHA1 для входной строки"""
    return hashlib.sha1(data_str.encode('utf-8')).hexdigest()

def create_transaction_string(txn_dict: dict) -> str:
    """
    Создает строку для хеширования путем конкатенации значений полей.
    Порядок полей фиксирован.
    """
    # порядок ключей 
    keys_order = [
        "txn_id", "timestamp", "borrower_id", "lender_id", 
        "amount", "currency", "term_months", "status"
    ]
    return "".join(str(txn_dict[key]) for key in keys_order)