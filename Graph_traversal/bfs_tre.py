from collections import deque
def bfs_tree(adj_list, start):
    """jhgjh"""
    n = len(adj_list) #no of vertices
    state = ['U'] * n
    parent  = [None] * n
    Q = deque()
    state[start] = 'D'
    Q.append(start)
    return bfs_loop(adj_list, Q, state, parent)
def bfs_loop(adj_list, Q, state, parent):
    """jhkj"""
    while len(Q) != 0:
        u = Q.popleft()
        for v in adj_list[u]:
            v = v[0]
            if state[v] == 'U':
                state[v] = 'D'
                parent[v] = u
                Q.append(v)
        state[u] = 'P'
    return parent

# an undirected graph

adj_list = [
    [(1, None)],
    [(0, None), (2, None)],
    [(1, None)]
]

print(bfs_tree(adj_list, 0))
print(bfs_tree(adj_list, 1))

# a directed graph (note the asymmetrical adjacency list) -------
# adj_list = [
# [(1, None)],
# []
# ]

# print(bfs_tree(adj_list, 0))
# print(bfs_tree(adj_list, 1))
