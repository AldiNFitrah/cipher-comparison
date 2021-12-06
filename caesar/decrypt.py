import timeit
from math import ceil

ITERATIONS = 5
N = 3
ord_0 = ord('0')
ord_9 = ord('9')

ord_A = ord('A')
ord_Z = ord('Z')

ord_a = ord('a')
ord_z = ord('z')


def decrypt(ciphertext, shift):
    plaintext = ""

    for cc in ciphertext:
        c = ord(cc)
        if ord_0 <= c <= ord_9:
            c -= shift
            c += 10 * (ceil((ord_0 - c) / 10))
        elif ord_A <= c <= ord_Z:
            c -= shift
            c += 26 * (ceil((ord_A - c) / 26))
        elif ord_a <= c <= ord_z:
            c -= shift
            c += 26 * (ceil((ord_a - c) / 26))

        plaintext += chr(c)

    return plaintext

for i in range(4, 6 + 1):
    for j in range(1, 50 + 1):
        in_file = open("encrypted/10^{}/{}.txt".format(i, j), encoding="utf-8")
        out_file = open("decrypted/10^{}/{}.txt".format(i, j), "w", encoding="utf-8")
        out_file_time = open("decrypted/10^{}/{}_time.txt".format(i, j), "w")

        total_duration = 0
        decrypted = ""
        plaintext = in_file.read()
        for _ in range(ITERATIONS):

            start = timeit.default_timer()
            decrypted = decrypt(plaintext, N)
            stop = timeit.default_timer()

            duration = (stop - start) * 1000
            total_duration += duration

        print(decrypted, file=out_file, end="")
        print(total_duration / ITERATIONS, file=out_file_time)

        in_file.close()
        out_file.close()
        out_file_time.close()
