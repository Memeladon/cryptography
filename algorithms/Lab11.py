import hashlib


def generate_md6_hash(text):
    # Преобразование текста в байты
    text_bytes = text.encode('utf-8')
    # Объект хэша SHA-256
    hash_object = hashlib.sha256(text_bytes)
    # Шестнадцатеричное представление хэша
    hex_dig = hash_object.hexdigest()
    return hex_dig


# Example usage
text = "Hello, world!"
hash_result = generate_md6_hash(text)
print(f"MD6 Хэш от '{text}': {hash_result}")
