def binary(symbol, sym_len):
    import numpy as np

    rand_n = np.random.rand(symbol)
    rand_n[np.where(rand_n >= 0.5)] = 1
    rand_n[np.where(rand_n <= 0.5)] = 0

    print(rand_n)

    sig = np.zeros(int(symbol*sym_len))

    id_1 = np.where(rand_n == 1)

    for i in id_1[0]:
        temp = int(i*sym_len)
        sig[temp:temp + sym_len] = 1
    print(sig)
    return sig