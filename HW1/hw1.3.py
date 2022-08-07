# File: hw1.3.py
# Author(s): xiongyuc, nkulukur, ppanda

# 3.a
import numpy as np


def price(i):
    if i >= 1 and i <= 4:
        return [0, 1, 5, 8, 9][i]
    return 0


M = {}     # dict of already computed (values,cuts)


def Rev(N):
    if N in M:
        return M[N]
    mxrev = 0
    cuts = []
    if N < 1:
        mxrev = price(N)
    else:
        for k in range(1, N+1):  # [1..N]
            checkval = price(k) + Rev(N-k)[0]
            if(checkval > mxrev):
                cuts = Rev(N-k)[1] + [k]
                mxrev = checkval
    M[N] = (mxrev, cuts)
    return M[N]


for i in range(21):
    print("Rev({:d}) = ".format(i), Rev(i))


# 3.b
A0 = np.array([[0, np.inf, np.inf, 1],
               [2, 0, 4, 5],
               [np.inf, np.inf, 0, 3],
               [np.inf, 7, 1, 0]])


def WSD(Graph):
    update = []
    graph = Graph.copy()
    for i in range(len(graph)):
        for j in range(len(graph)):
            for k in range(len(graph)):
                graph[j, k] = min(graph[j, k], graph[j, i] + graph[i, k])
        update.append(graph)
    return update


# Display A_4
A4 = WSD(A0)[-1]
print('A4: ')
print(A4)

# 3.c
A0 = np.array([[0, 6, np.inf, 1, np.inf, np.inf, 3],
               [np.inf, 0, 2, np.inf, np.inf, 4, np.inf],
               [np.inf, np.inf, 0, 4, np.inf, np.inf, np.inf],
               [np.inf, np.inf, np.inf, 0, 10, np.inf, 2],
               [np.inf, np.inf, 1, np.inf, 0, 1, np.inf],
               [np.inf, np.inf, 4, np.inf, 1, 0, np.inf],
               [2, 1, np.inf, np.inf, np.inf, np.inf, 0]])
# Display A_7
A7 = WSD(A0)[-1]
print('A7: ')
print(A7)
