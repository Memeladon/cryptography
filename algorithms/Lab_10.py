# № 10 Реализовать криптосистему Рабина для шифрования и расшифрования вводимых сообщений.
# Открытый ключ показывать пользователю, закрытый ключ записывать в файл.
from sympy import nextprime


class RabinCrypto:
    def __init__(self, start_num=100000):
        self.__p = self.generate_prime(start_num)
        self.__q = self.generate_prime(self.__p)

        while self.__p % 4 != 3 or self.__q % 4 != 3:
            self.__p = self.generate_prime(self.__p)
            self.__q = self.generate_prime(self.__q)

        self.n = self.__p * self.__q
        print(f"public_key: {self.n}, private key: {self.__p, self.__q}")

    @staticmethod
    def generate_prime(n):
        return nextprime(n)

    @staticmethod
    def half_extended_euclidean(a, b):
        """
        https://crypto.stackexchange.com/questions/54444/how-to-optimise-euclidean-algorithm-for-large-numbers-rsa
        :return: m, x, y , где ax+by=НОД(a,b), m - изначальный модуль
        """
        x, y, m = 0, 1, b

        while True:
            if a == 1:
                return m, x, y
            elif a == 0:
                return None

            q = b // a
            b, x = b - a * q, x + q * y

            if b == 1:
                return m - x, x, y
            elif b == 0:
                return None

            q = a // b
            a, y = a - b * q, y + q * x

    def encrypt(self, message):
        # Преобразование в двоичный формат и расширение
        message = int.from_bytes(message.encode(), 'big')

        if message >= self.n:
            raise ValueError("Сообщение больше чем public_key")
        return pow(message, 2, self.n)  # ciphertext

    def decrypt_one(self, ciphertext):
        p1 = pow(ciphertext, (self.__p + 1) // 4, self.__p)
        p2 = self.__p - p1
        q1 = pow(ciphertext, (self.__q + 1) // 4, self.__q)
        q2 = self.__q - q1
        possibilities = [p1, p2, q1, q2]

        print(possibilities)
        for m in possibilities:
            if pow(m, 2, self.n) == ciphertext:
                return m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()

    def decrypt_two(self, ciphertext):
        mq = pow(ciphertext, (self.__p + 1) // 4, self.__q)
        mp = pow(ciphertext, (self.__p + 1) // 4, self.__p)

        _, yp, yq = self.half_extended_euclidean(self.__p, self.__q)

        r1 = pow((yp * self.__p * mq + yq * self.__q * mp), 1, self.n)
        r2 = self.n - r1
        r3 = pow((yp * self.__p * mq - yq * self.__q * mp), 1, self.n)
        r4 = self.n - r3
        result = [r1, r2, r3, r4]

        print(result)
        for m in result:
            if pow(m, 2, self.n) == ciphertext:
                return m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()


Encrypt = RabinCrypto()
ciphertext = Encrypt.encrypt('20')
print('Способ 1:', Encrypt.decrypt_one(ciphertext), 'Способ 2:', Encrypt.decrypt_two(ciphertext))
