RU_ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
ALPHABET_SIZE = len(RU_ALPHABET)

def char_to_index(char: str) -> int:
    """символ в индекс в алфавите"""
    try:
        return RU_ALPHABET.index(char.upper())
    except ValueError:
        raise ValueError(f"Символ '{char}' отсутствует в русском алфавите")

def index_to_char(index: int) -> str:
    """индекс в символ алфавита"""
    return RU_ALPHABET[index % ALPHABET_SIZE]

def vigenere_encrypt(plaintext: str, key: str) -> str:
    """Шифрование шифром Виженера"""
    ciphertext = []
    key_idx = 0
    for char in plaintext:
        if char.upper() in RU_ALPHABET:
            m_idx = char_to_index(char)
            k_idx = char_to_index(key[key_idx])
            
            # Формула шифрования: Ci = (Mi + Ki) mod N
            c_idx = (m_idx + k_idx) % ALPHABET_SIZE
            ciphertext.append(index_to_char(c_idx))
            
            key_idx = (key_idx + 1) % len(key)
        else:
            ciphertext.append(char) 
    return "".join(ciphertext)

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    """Расшифрование шифром Виженера"""
    plaintext = []
    key_idx = 0
    for char in ciphertext:
        if char.upper() in RU_ALPHABET:
            c_idx = char_to_index(char)
            k_idx = char_to_index(key[key_idx])
            
            # Формула расшифровки: Mi = (Ci - Ki) mod N
            m_idx = (c_idx - k_idx) % ALPHABET_SIZE
            plaintext.append(index_to_char(m_idx))
            
            key_idx = (key_idx + 1) % len(key)
        else:
            plaintext.append(char)
    return "".join(plaintext)