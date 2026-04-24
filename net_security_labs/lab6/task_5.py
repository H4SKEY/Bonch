from utils import lagrange_interpolation_secret

# Исходные данные
p = 53
# Выбираем 4 доли (больше порога k=3)
# Например: (1, 39), (2, 0), (3, 20), (4, 46)
selected_shares = [(1, 39), (2, 0), (3, 20), (4, 46)]

print(f"--- Задание 5: Восстановление по 4 долям ---")
print(f"Используемые доли: {selected_shares}")

recovered_secret = lagrange_interpolation_secret(selected_shares, p)

print(f"Восстановленный секрет: {recovered_secret}")
if recovered_secret == 31:
    print("УСПЕХ: Секрет совпадает с исходным (31). Избыточность данных не повлияла на результат.")
else:
    print("ОШИБКА: Секрет не совпадает.")