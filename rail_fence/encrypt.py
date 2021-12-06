import timeit

ITERATIONS = 5
N = 3

def encrypt(plaintext, num_of_rails):
    rails = ["" for _ in range(num_of_rails)]
    rails_index = 0
    rails_direction = 1

    for char in plaintext:
        rails[rails_index] += char
        rails_index += rails_direction

        if rails_index == num_of_rails - 1:
            rails_direction = -1
        elif rails_index == 0:
            rails_direction = 1

    result = ""
    for rail in rails:
        result += rail

    return result

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
            encrypted = encrypt(plaintext, N)
            stop = timeit.default_timer()

            duration = (stop - start) * 1000
            total_duration += duration

        print(encrypted, file=out_file, end="")
        print(total_duration / ITERATIONS, file=out_file_time)

        in_file.close()
        out_file.close()
        out_file_time.close()