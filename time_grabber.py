from pprint import pprint


with open('out.txt', 'w') as f:
    for a in ["caesar", "vigenere", "mercurial", "rail_fence"]:
        for m in ["encrypted", "decrypted"]:
            time = {
                "10^4": [],
                "10^5": [],
                "10^6": [],
            }
            for i in range(4, 6 + 1):
                for j in range(1, 50 + 1):
                    with open('{}/{}/10^{}/{}_time.txt'.format(a, m, i, j), 'r') as file:
                        value = file.read().strip()
                        time["10^{}".format(i)].append(float(value))

            print("{}_{}".format(a[0], m[0]), end=" = ", file=f)
            pprint(time, stream=f)
