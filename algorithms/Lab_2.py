from .Lab_1 import Lab_1


class Lab_2(Lab_1):
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Lab_2, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def chinese_remainder_theorem(a: list, m: list) -> (int, int):
        """
        Реализует китайскую теорему об остатках для системы сравнений x ≡ a_i (mod m_i).
        Вычисляет значение x и M, где x - решение системы, а M - произведение всех модулей.
        Возвращает кортеж из значений x и M.
        :param a: Массив остатков
        :param m: Массив делителей
        :return: Кортеж из значений x и M
        """
        M = 1
        for mi in m:
            M *= mi
        print("M:", M, '\n')

        x = 0
        for ai, mi in zip(a, m):
            Mi = M // mi
            print("Mi = ", Mi)
            inv = Lab_1.find_inverse_element(Mi, mi)
            print("Mi^-1 = ", inv)
            x += ai * Mi * inv

        return x % M, M

    @staticmethod
    def solve_system_of_congruences(a: list, m: list):
        """
        Это функция для решения системы сравнений.
        Проверяет, что количество сравнений и модулей одинаково и что модули попарно взаимно просты (НОД каждых двух модулей равен 1).
        Использует китайскую теорему об остатках для решения системы сравнений.
        Если решения существуют, возвращает список всех решений, иначе генерирует исключение.
        :param a: Массив остатков
        :param m: Массив делителей
        :return: Массив решений
        """
        n = len(a)
        if n != len(m):
            raise ValueError("Число конгруэнций и модулей должно быть одинаковым")

        # Попарная простота
        for i in range(n):
            for j in range(i + 1, n):
                print(f"НОД{(m[i], m[j])} = ", Lab_1.gcd(m[i], m[j]))
                if Lab_1.gcd(m[i], m[j]) != 1:
                    raise ValueError("Модули не являются попарно простыми")

        solution, M = Lab_2.chinese_remainder_theorem(a, m)
        return solution, M
