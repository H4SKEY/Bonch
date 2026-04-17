from utils import vigenere_encrypt, vigenere_decrypt

# Исходные данные
full_name = "СЕРОВ АНТОН АЛЕКСАНДРОВИЧ"
key = "ПСЖ"

print(f"Открытый текст: {full_name}")
print(f"Ключ: {key}")

# Задание 2: Шифрование
encrypted_text = vigenere_encrypt(full_name, key)
print(f"\nЗашифрованный текст: {encrypted_text}")

# Задание 3: Расшифрование (проверка)
decrypted_text = vigenere_decrypt(encrypted_text, key)
print(f"Расшифрованный текст: {decrypted_text}")

# Проверка совпадения
if decrypted_text.upper() == full_name.upper():
    print("\nПроверка пройдена успешно: исходный и расшифрованный тексты совпадают.")
else:
    print("\nОшибка: тексты не совпадают!")