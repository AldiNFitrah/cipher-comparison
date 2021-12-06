import timeit
from math import ceil

ITERATIONS = 5
KEY = "LOVE"

ord_0 = ord('0')
ord_9 = ord('9')

ord_A = ord('A')
ord_Z = ord('Z')

ord_a = ord('a')
ord_z = ord('z')

def encrypt(plaintext, key):
    ciphertext = ""
    key_length = len(key)

    for i in range(len(plaintext)):
        c = ord(plaintext[i])
        k = ord(key[i % key_length])

        shift = 0
        if ord_0 <= k <= ord_9:
            shift = k - ord_0
        elif ord_A <= k <= ord_Z:
            shift = k - ord_A
        elif ord_a <= k <= ord_z:
            shift = k - ord_a

        if ord_0 <= c <= ord_9:
            c += shift
            c -= 10 * (ceil((c - ord_9) / 10))

        elif ord_A <= c <= ord_Z:
            c += shift
            c -= 26 * (ceil((c - ord_Z) / 26))

        elif ord_a <= c <= ord_z:
            c += shift
            c -= 26 * (ceil((c - ord_z) / 26))

        ciphertext += chr(c)

    return ciphertext

for i in range(4, 6 + 1):
    for j in range(1, 50 + 1):
        in_file = open("../input/10^{}/{}.txt".format(i, j))
        out_file = open("encrypted/10^{}/{}.txt".format(i, j), "w", encoding="utf-8")
        out_file_time = open("encrypted/10^{}/{}_time.txt".format(i, j), "w")

        total_duration = 0
        encrypted = ""
        plaintext = in_file.read()
        for _ in range(ITERATIONS):
            start = timeit.default_timer()
            encrypted = encrypt(plaintext, KEY)
            stop = timeit.default_timer()

            duration = (stop - start) * 1000
            total_duration += duration

        print(encrypted, file=out_file, end="")
        print(total_duration / ITERATIONS, file=out_file_time)

        in_file.close()
        out_file.close()
        out_file_time.close()
