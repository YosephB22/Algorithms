from adjacency_list import *
    
def dfs_tree(adj_list, start):
    """jhgjh"""
    adjacent_list = adjacency_list(adj_list)
    n = len(adjacent_list) #no of vertices
    state = ['U'] * n
    parent  = [None] * n
    state[start] = 'D'
    dfs_loop(adjacent_list, start, state, parent)
    return parent
def dfs_loop(adjacent_list, u, state, parent):
    """jhkj"""
    for v in adjacent_list[u]:
        v = v[0]
        if state[v] == 'U':
            state[v] = 'D'
            parent[v] = u
            dfs_loop(adjacent_list, v, state, parent)
    state[u] = 'P'

# graph from the textbook example
graph_string = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

print(dfs_tree(graph_string, 1))