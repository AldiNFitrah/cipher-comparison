from pprint import pprint
import timeit

ITERATIONS = 5
N = 3


def decrypt(ciphertext, num_of_rails):
    rails = [
        [None for i in range(len(ciphertext))] for j in range(num_of_rails)
    ]

    direction = 1
    row, col = 0, 0

    for i in range(len(ciphertext)):
        if row == 0:
            direction = 1
        if row == num_of_rails - 1:
            direction = -1

        rails[row][col] = 0
        col += 1
        row += direction

    index = 0
    for i in range(num_of_rails):
        for j in range(len(ciphertext)):
            if ((rails[i][j] == 0) and (index < len(ciphertext))):
                rails[i][j] = ciphertext[index]
                index += 1

                if index >= len(ciphertext):
                    break

        if index >= len(ciphertext):
            break

    plaintext = ""
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            direction = 1
        if row == num_of_rails-1:
            direction = -1

        if (rails[row][col] != 0):
            plaintext += rails[row][col]
            col += 1

        row += direction

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
