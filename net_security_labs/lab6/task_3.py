from utils import lagrange_interpolation_secret

# Исходные данные
p = 53
# Выбираем любые 3 доли из полученных в задании 2
# Например: (1, 39), (2, 0), (3, 20)
selected_shares = [(1, 39), (2, 0), (3, 20)]

print(f"--- Задание 3: Восстановление по 3 долям ---")
print(f"Используемые доли: {selected_shares}")

recovered_secret = lagrange_interpolation_secret(selected_shares, p)

print(f"Восстановленный секрет: {recovered_secret}")
if recovered_secret == 31:
    print("УСПЕХ: Секрет совпадает с исходным (31)")
else:
    print("ОШИБКА: Секрет не совпадает.")