import random
import string

for j in range(4, 6 + 1):
    N = 10**j
    for i in range(1, 50 + 1):
        with open(f'caesar/input/10^{j}/{i}.txt', 'w') as f:
            s = ''.join(random.choices(string.ascii_uppercase, k=N))
            print(s, file=f, end="")
