from utils import lagrange_interpolation_secret

# Исходные данные
p = 53
# Выбираем 2 доли (меньше порога k=3)
# Например: (1, 39), (2, 0)
selected_shares = [(1, 39), (2, 0)]

print(f"--- Задание 4: Попытка восстановления по 2 долям ---")
print(f"Используемые доли: {selected_shares}")
print("Теоретически восстановление невозможно однозначно.")

recovered_val = lagrange_interpolation_secret(selected_shares, p)

print(f"Результат интерполяции (неверный секрет): {recovered_val}")

if recovered_val != 31:
    print("ПОДТВЕРЖДЕНО: Полученное значение не равно секрету (31). Восстановление безуспешно.")
else:
    print("Случайное совпадение (маловероятно).")