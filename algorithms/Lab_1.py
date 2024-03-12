class Lab_1:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Lab_1, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def gcd(a: int, b: int) -> int:
        """
        gcd_2 (Итеративный алгоритм Евклида):
        Итеративный алгоритм Евклида также эффективен и имеет сложность O(log(min(a, b))).
        Не использует рекурсию и избегает проблем с глубиной стека.
        :param b: int
        :param a: int
        :return: НОД
        """
        while b:
            a, b = b, a % b
        return a

    @staticmethod
    def extended_gcd(a, b) -> tuple[int, int, int]:
        """
        Функция, которая реализует расширенный алгоритм Евклида.
        Этот алгоритм находит наибольший общий делитель (НОД) двух чисел
        и одновременно находит их линейные комбинации, такие что ax+by=НОД(a,b) это (Коэффициенты Безу)
        :param b: int
        :param a: int
        :return НОД, x, y
        """
        if a == 0:
            return b, 0, 1
        else:
            gcd_value, x, y = Lab_1.extended_gcd(b % a, a)
            return gcd_value, y - (b // a) * x, x

    @staticmethod
    def find_inverse_element(a: int, m: int):
        """
         функция находит обратный элемент для a (mod m) с использованием расширенного алгоритма Евклида
         :param a: int
         :param m: int
         :return Элемент обратный x по модулю m
        """
        _, x, _ = Lab_1.extended_gcd(a, m)
        return x % m

    @staticmethod
    def phi(n: int):
        """
        Вычисление функции Эйлера
        :param n: int
        :return Значение функции Эйлера для числа n
        """
        if n is not int:
            print('Параметр [n] не определен на множестве простых чисел!')
            return TypeError
        result = 1
        for i in range(2, n):
            if Lab_1.gcd(i, n) == 1:
                result += 1
        print(f"Функция Эйлера φ({n}) = {result}")
        return result

    @staticmethod
    def is_primitive_root(g: int, m: int):
        """
        :param g: int
        :param m: int
        :return: Является ли g первообразным корнем по модулю m
        """
        powers = set()
        for i in range(1, m):
            powers.add(pow(g, i, m))
        # print(powers)
        return len(powers) == m - 1

    @staticmethod
    def find_primitive_roots(m: int):
        """
        Находит все первообразные корни по модулю m
        :param m: int
        :return: Все первообразные корни (mod m)
        """
        primitive_roots = []
        for g in range(2, m):
            if Lab_1.is_primitive_root(g, m):
                primitive_roots.append(g)

        print(f"Все первообразные корни (mod {m}): ", primitive_roots)
        return primitive_roots

    @staticmethod
    def linear_diophantine(a: int, b: int, c: int):
        """
        Метод решения диофантовых уравнений первой степени с помощью расширенного алгоритма Евклида
        :param a: int
        :param b: int
        :param c: int
        :return: Частные решения x0, y0
        """
        gcd_value, x, y = Lab_1.extended_gcd(a, b)

        if c % gcd_value != 0:
            print(f"Решение уравнения {a}x + {b}y = {c} отсутствует")
            return None

        # Частное решение (x0, y0) однородного уравнения ax + by = gcd(a, b)
        x0 = x * (c // gcd_value)
        y0 = y * (c // gcd_value)

        print(f"Решение уравнения {a}x + {b}y = {c}: (x = {x0}, y = {y0})")
        return x0, y0

    @staticmethod
    def solve_linear_congruence(a: int, b: int, m: int):
        """
         Решает сравнение ax ≡ b (mod m)
        :param b: int
        :param a: int
        :param m: int
        :return Решение сравнения - x
        """

        # Метод умножения на обратный элемент
        a_inv = Lab_1.find_inverse_element(a, m)
        x_inv = (a_inv * b) % m

        print(f"Решение сравнения {a}x ≡ {b} (mod {m}): (x ≡ {x_inv} (mod {m}))")

        return x_inv
