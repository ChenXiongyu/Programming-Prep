
# breadth_first_search.py
# Author(s): xiongyuc, nkulukur, ppanda

# # 2.a (function definition)
# '''
# def BFS(G, root, target): # Pythonish pseudocode
#    S.add(root)
#    T.add(root, None)      # value, parent
#    Q = [root]
#    while Q:
#       cur = Q.pop(0)
#       if cur is target:
#          return cur parent list
#       for v in G[cur]:
#          if v not in S:
#             S.add(v)
#             T.add(v, cur)
#             Q += [v]
# '''


class ParentTree:
    def __init__(self, root):
        self.tree = {root: None}
        
    def add(self, node, par):
        self.tree[node] = par


def BFS(G, root, target):
    S = set()
    S.add(root)
    T = ParentTree(root)
    Q = [root]
    while Q:
        cur = Q.pop(0)
        if cur == target:
            parents = [cur]
            while True:
                parent = T.tree[cur]
                if parent:
                    parents.append(parent)
                    cur = parent
                else:
                    return parents[::-1]
        for v in G[cur]:
            if v not in S:
                S.add(v)
                T.add(v, cur)
                Q.append(v)
    if( target == None ):
        Conn_Comp = list(T.tree.keys())
        Conn_Comp.sort()
        return Conn_Comp


# # 2.c (function definitions)

def BFS_con_comps(G):
    # return a list of connected components in G,
    # where each connected component is a sorted list of nodes
    nodes = list(G.keys())
    nodes.sort()
    G_cc = []
    visited = []
    for node in nodes:
        if node not in visited:
            cc = BFS( G, node, None)
            visited += cc
            G_cc += [cc]
    return G_cc


def print_con_comps(G_cc):  # display connected components
    print('graph contains', len(G_cc), 'connected components:')
    for i in range(len(G_cc)):    
        print('    {:d}: '.format(i + 1), end='')
        print(G_cc[i])


def main():

    # 2.a (test code)
    G = {   'A' : [ 'B', 'J', 'Me' ],
            'B' : [ 'A' ],
            'C' : [ 'D', 'P' ],
            'D' : [ 'C', 'O' ],
            'E' : [ 'F', 'J', 'K' ],
            'F' : [ 'E', 'M' ],
            'G' : [ 'K', 'S', 'Ed' ],
            'H' : [ 'O', 'U' ],
            'Me': [ 'A', 'I', 'N', 'V' ],
            'I' : [ 'Me', 'Q' ],
            'J' : [ 'A', 'E', 'L', 'Q', 'W' ],
            'K' : [ 'E', 'G' ],
            'L' : [ 'J', 'W' ],
            'M' : [ 'E', 'S', 'T' ],
            'N' : [ 'Me', 'V' ],
            'O' : [ 'H', 'D' ],
            'P' : [ 'C', 'U' ],
            'Q' : [ 'I', 'J', 'X', 'Y' ],
            'R' : [ 'Ed' ],
            'S' : [ 'G', 'M', 'Y', 'Z' ],
            'T' : [ 'M' ],
            'U' : [ 'H', 'P' ],
            'V' : [ 'Me', 'N' ],
            'W' : [ 'J', 'L' ],
            'X' : [ 'Q', 'Y' ],
            'Y' : [ 'Q', 'S', 'X', 'Z' ],
            'Ed': [ 'G', 'R', 'Z' ],
            'Z' : [ 'S', 'Y', 'Ed' ] }
    print('Shortest path from Me to Ed:', BFS(G, 'Me', 'Ed'))

    # 2.b (test code)
    print('Shortest path from A to I:  ', BFS(G, 'A', 'I'))
    print('Shortest path from B to R:  ', BFS(G, 'B', 'R'))
    print('Shortest path from C to H:  ', BFS(G, 'C', 'H'))
    print('Shortest path from M to T:  ', BFS(G, 'M', 'T'))

    # 2.c (test code)

    # connected components tests:
    G2 = {  'A': ['B', 'C'],
            'C': ['A'],
            'E': ['F'],
            'D': [],
            'B': ['A'],
            'F': ['E'] }
    G2_cc = BFS_con_comps(G2)
    print_con_comps(G2_cc)
    G_cc = BFS_con_comps(G)
    print_con_comps(G_cc)


if __name__ == '__main__':
    main()
