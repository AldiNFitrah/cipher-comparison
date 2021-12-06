import timeit

MAC_ADDRESS = "983B8F1B850A"
KEY1 = "k2k9vpibbaej8q0oetotrcxfdpkq0exbjtz4"
KEY2 = MAC_ADDRESS
ITERATIONS = 5


def decrypt(ciphertext, key1, key2):
    plaintext = ""

    for i in range(len(ciphertext)):
        int_val = (ord(ciphertext[i]) ^ (ord(key2[i % len(key2)]))) // (ord(key1[i % len(key1)]) + i % len(key1))
        plaintext += chr(int_val)

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
            decrypted = decrypt(plaintext, KEY1, KEY2)
            stop = timeit.default_timer()

            duration = (stop - start) * 1000
            total_duration += duration

        print(decrypted, file=out_file, end="")
        print(total_duration / ITERATIONS, file=out_file_time)

        in_file.close()
        out_file.close()
        out_file_time.close()
