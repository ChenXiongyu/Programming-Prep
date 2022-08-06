# 3.a
def price(i):
    if 1 <= i <= 4:
        return [0, 1, 5, 8, 9][i]
    return 0


M = {}
Method = {}
def Rev(N):
    if N in M:
        return M[N], Method[N]
    mxrev = 0
    if N <= 1:
        mxrev = price(N)
        method = [N]
    else:
        for k in range(1, N + 1):
            potential = Rev(N - k)
            if mxrev < potential[0] + price(k):
                mxrev = potential[0] + price(k)
                method = potential[1]
                method.append(k)
    if N > 0:
        try:
            method.remove(0)
        except ValueError:
            pass
    M[N] = mxrev
    Method[N] = method
    return mxrev, method


for N in range(21):
    print('N: {:d}'.format(N))
    result = Rev(N)
    print('Maximum Revenue: {:d}'.format(result[0]))
    print('Cuts: ', result[1])
    
    
# 3.b
import numpy as np
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
