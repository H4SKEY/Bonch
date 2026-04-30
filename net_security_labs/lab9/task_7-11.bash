# 1. Просмотр параметров кривой (Задание 7)
openssl ecparam -name secp384r1 -noout -text

# 2. Генерация закрытого ключа (Задание 8)
openssl ecparam -name secp384r1 -genkey -noout -out private_key.pem

# 3. Получение открытого ключа (Задание 8)
openssl ec -in private_key.pem -pubout -out public_key.pem

# 4. Создание файла с данными (Задание 9)
echo -e "Фамилия: Серов\nИмя: Антон\nОтчество: Александрович\nГруппа: ИКВТ-42\nВариант: 7" > student_info.txt

# 5. Подпись файла (Задание 10). Используем sha1 как наиболее совместимый аналог из задания.
openssl dgst -sha1 -sign private_key.pem -out signature.bin student_info.txt

# 6. Проверка подписи исходного файла (Задание 11)
echo "Tampered" >> student_info.txt
openssl dgst -sha1 -verify public_key.pem -signature signature.bin student_info.txt
