import timeit

MAC_ADDRESS = "983B8F1B850A"
KEY1 = "k2k9vpibbaej8q0oetotrcxfdpkq0exbjtz4"
KEY2 = MAC_ADDRESS
ITERATIONS = 5


def encrypt(plaintext, key1, key2):
    ciphertext = ""

    for i in range(len(plaintext)):
        int_val = (ord(plaintext[i]) * (ord(key1[i % len(key1)]) + i % len(key1))) ^ ord(key2[i % len(key2)])
        ciphertext += chr(int_val)

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
            encrypted = encrypt(plaintext, KEY1, KEY2)
            stop = timeit.default_timer()

            duration = (stop - start) * 1000
            total_duration += duration

        print(encrypted, file=out_file, end="")
        print(total_duration / ITERATIONS, file=out_file_time)

        in_file.close()
        out_file.close()
        out_file_time.close()
