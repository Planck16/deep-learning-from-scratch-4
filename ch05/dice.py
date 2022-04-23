import numpy as np


def sample(dice=2):
    x = 0
    for _ in range(dice):
        x += np.random.choice([1, 2, 3, 4, 5, 6])
    return x


if __name__ == '__main__':
    trial = 1000
    V = 0
    n = 0

    for _ in range(trial):
        s = sample()
        n += 1
        V += (s - V) / n
        print(V)