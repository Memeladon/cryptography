"""
Реализовать программный продукт, позволяющий шифровать и
расшифровывать сообщения на русском языке с помощью RC6. Чтение
открытого текста и шифртекста должно быть возможно с клавиатуры, запись
результата шифрования/расшифрования на экран. Ключ формируется
автоматически и сохраняется на весь сеанс шифрования. Ключ сохраняется в
отдельный файл. Для реализации криптоалгоритмов запрещено пользоваться
встроенными библиотеками используемых языков
"""

# Параметры RC6
w = 32 # размер слова в битах
r = 20 # количество раундов
b = 16 # количество байтов в ключе
key = bytearray(b) # ключ (инициализируется пустыми байтами)

# Расширение ключа
def key_expansion(key):
    L = [int.from_bytes(key[i:i + 4], 'little') for i in range(0, len(key), 4)]
    c = len(key) // 4
    const = 0xB7E15163
    S = [(const * i) & (2 ** 32 - 1) for i in range(2 * r + 4)]
    i, j = 0, 0
    A, B = 0, 0
    for _ in range(3 * max(c, 2 * r + 4)):
        A = S[i] = (S[i] + A + B) & (2 ** 32 - 1)
        B = L[j] = (L[j] + A + B) & (2 ** 32 - 1)
        i = (i + 1) % (2 * r + 4)
        j = (j + 1) % c
    return S

# Шифрование RC6
def rc6_encrypt(plaintext, key):
    S = key_expansion(key)
    plaintext = pad(plaintext)
    blocks = [plaintext[i:i + 16] for i in range(0, len(plaintext), 16)]
    encrypted_blocks = []
    for block in blocks:
        A, B, C, D = [int.from_bytes(block[i:i + 4], 'little') for i in range(0, 16, 4)]
        B = (B + S[0]) & (2 ** 32 - 1)
        D = (D + S[1]) & (2 ** 32 - 1)
        for i in range(1, r + 1):
            t = (B * (2 * B + 1)) & (2 ** w - 1)
            u = (D * (2 * D + 1)) & (2 ** w - 1)
            A = ((A ^ t) + S[2 * i]) & (2 ** 32 - 1)
            C = ((C ^ u) + S[2 * i + 1]) & (2 ** 32 - 1)
            A, B, C, D = B, C, D, A
        C = (C + S[2 * r + 2]) & (2 ** 32 - 1)
        D = (D + S[2 * r + 3]) & (2 ** 32 - 1)
        encrypted_blocks.append(b''.join([A.to_bytes(4, 'little'), B.to_bytes(4, 'little'),
                                          C.to_bytes(4, 'little'), D.to_bytes(4, 'little')]))
    return b''.join(encrypted_blocks)

# Расшифрование RC6
def rc6_decrypt(ciphertext, key):
    S = key_expansion(key)
    blocks = [ciphertext[i:i + 16] for i in range(0, len(ciphertext), 16)]
    decrypted_blocks = []
    for block in blocks:
        A, B, C, D = [int.from_bytes(block[i:i + 4], 'little') for i in range(0, 16, 4)]
        C = (C - S[2 * r + 2]) & (2 ** 32 - 1)
        D = (D - S[2 * r + 3]) & (2 ** 32 - 1)
        for i in range(r, 0, -1):
            A, B, C, D = D, A, B, C
            u = (D * (2 * D + 1)) & (2 ** w - 1)
            t = (B * (2 * B + 1)) & (2 ** w - 1)
            C = ((C - S[2 * i + 1]) ^ u) & (2 ** 32 - 1)
            A = ((A - S[2 * i]) ^ t) & (2 ** 32 - 1)
        D = (D - S[1]) & (2 ** 32 - 1)
        B = (B - S[0]) & (2 ** 32 - 1)
        decrypted_blocks.append(b''.join([A.to_bytes(4, 'little'), B.to_bytes(4, 'little'),
                                          C.to_bytes(4, 'little'), D.to_bytes(4, 'little')]))
    plaintext = b''.join(decrypted_blocks)
    # Удаление дополнения
    pad_len = plaintext[-1]
    return plaintext[:-pad_len]

# Дополнение открытого текста до кратного 16 байтам
def pad(plaintext):
    pad_len = 16 - (len(plaintext) % 16)
    return plaintext + bytes([pad_len] * pad_len)

# Получение ввода от пользователя
plaintext = input("Введите сообщение для шифрования: ").encode('utf-8')

# Генерация ключа (случайные байты)
import os

if not os.path.exists('rc6_key.txt'):
    key = os.urandom(b)
    with open('rc6_key.txt', 'wb') as key_file:
        key_file.write(key)
else:
    with open('rc6_key.txt', 'rb') as key_file:
        key = key_file.read()

# Шифрование открытого текста
encrypted = rc6_encrypt(plaintext, key)
print("Зашифрованное сообщение:", encrypted.hex())

# Расшифрование шифртекста
decrypted = rc6_decrypt(encrypted, key)
print("Расшифрованное сообщение:", decrypted.decode('utf-8'))
