from algorithms import *


# ~~~~~~~~~~~~~~~~~~~~~~~ Демонстрация первой лабы ~~~~~~~~~~~~~~~~~~~~~~~ #
def first():
    print('/////////////////////////////////////////////////////////////////////////////////////////////')
    a = 3
    b = 34
    print(f'НОД{a,b} = ', Lab_1.gcd(a, b))  # НОД
    Lab_1.phi(243)  # Функция Эйлера
    Lab_1.find_primitive_roots(11)
    print()
    Lab_1.linear_diophantine(4, 3, 7)  # ax + bx = c (Способ расширенного алгоритма Евклида)
    print()
    Lab_1.solve_linear_congruence(3, 19, 34)  # Сравнение ax ≡ b (mod m)
    print('/////////////////////////////////////////////////////////////////////////////////////////////')
    Lab_1.linear_diophantine(15, 25, 69)  # ax + bx = c (Способ расширенного алгоритма Евклида)


# ~~~~~~~~~~~~~~~~~~~~~~~ Демонстрация второй лабы ~~~~~~~~~~~~~~~~~~~~~~~ #
def second():
    a = [7, -1, 3]
    m = [8, 11, 15]

    print("Решения сравнений:")
    for ai, mi in zip(a, m):
        print(f"x ≡ {ai} mod {mi}")
    print()

    try:
        solution, M = Lab_2.solve_system_of_congruences(a, m)
        print("\nРешение системы сравнений:")
        print(f"x ≡ {solution} mod {M}")
    except ValueError as e:
        print("Ошибка:", e)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Вызов лаб ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
first()
# second()
