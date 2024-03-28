"""
В описываемом алгоритме блок, подлежащий зашифровыванию (напомню, его длина 64 бита),
разделяется на две равные по длине (32 бита) части — правую и левую. Далее выполняется тридцать две итерации
 с использованием итерационных ключей, получаемых из исходного 256-битного ключа шифрования.


"""

BLOCK_SIZE = 4


def GOST_Magma_Add(a, b):
    c = bytearray(BLOCK_SIZE)
    for i in range(BLOCK_SIZE):
        c[i] = a[i] ^ b[i]
    return c


def GOST_Magma_Add_32(a, b):
    c = bytearray(BLOCK_SIZE)
    internal = 0
    for i in range(BLOCK_SIZE - 1, -1, -1):
        internal = a[i] + b[i] + (internal >> 8)
        c[i] = internal & 0xff
    return c


Pi = [
    [1, 7, 14, 13, 0, 5, 8, 3, 4, 15, 10, 6, 9, 12, 11, 2],
    [8, 14, 2, 5, 6, 9, 1, 12, 15, 4, 11, 0, 13, 10, 3, 7],
    [5, 13, 15, 6, 9, 2, 12, 10, 11, 7, 8, 1, 4, 3, 14, 0],
    [7, 15, 5, 10, 8, 1, 6, 13, 0, 9, 3, 14, 11, 4, 2, 12],
    [12, 8, 2, 1, 13, 4, 15, 6, 7, 0, 10, 5, 3, 14, 9, 11],
    [11, 3, 5, 8, 2, 15, 10, 13, 14, 1, 7, 4, 12, 9, 6, 0],
    [6, 8, 2, 3, 9, 10, 5, 12, 1, 14, 4, 7, 11, 13, 0, 15],
    [12, 4, 6, 2, 10, 5, 11, 9, 14, 8, 13, 7, 0, 3, 15, 1]
]


def GOST_Magma_T(in_data):
    out_data = bytearray(BLOCK_SIZE)
    for i in range(BLOCK_SIZE):
        first_part_byte = (in_data[i] & 0xf0) >> 4
        sec_part_byte = (in_data[i] & 0x0f)
        first_part_byte = Pi[i * 2][first_part_byte]
        sec_part_byte = Pi[i * 2 + 1][sec_part_byte]
        out_data[i] = (first_part_byte << 4) | sec_part_byte
    return out_data


# Пример использования функций:

a = bytearray([0x12, 0x34, 0x56, 0x78])
b = bytearray([0xAB, 0xCD, 0xEF, 0x90])

c = GOST_Magma_Add(a, b)
print("GOST_Magma_Add:", c.hex())

d = GOST_Magma_Add_32(a, b)
print("GOST_Magma_Add_32:", d.hex())

e = GOST_Magma_T(a)
print("GOST_Magma_T:", e.hex())
