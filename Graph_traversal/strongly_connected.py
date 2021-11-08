def adjacency_list(graph_str):
    header, *edges = [edge.split() for edge in graph_str.splitlines()]
    n = int(header[1])
    adja_list = [[] for _ in range(n)]
    for ed in edges:
        if len(header) == 2: # not weighted graph
            if header[0] == 'D':
                adja_list[int(ed[0])].append((int(ed[1]), None))
            else:
                adja_list[int(ed[0])].append((int(ed[1]), None))
                adja_list[int(ed[1])].append((int(ed[0]), None))
        else:
            if header[0] == 'D':
                adja_list[int(ed[0])].append((int(ed[1]), int(ed[2])))
            else:
                adja_list[int(ed[0])].append((int(ed[1]), int(ed[2])))
                adja_list[int(ed[1])].append((int(ed[0]), int(ed[2])))
    return adja_list

def dfs_tree(adj_list, start):
    """jhgjh"""
    n = len(adj_list) #no of vertices
    state = ['U'] * n
    parent  = [None] * n
    state[start] = 'D'
    dfs_loop(adj_list, start, state, parent)
    return state
def dfs_loop(adj_list, u, state, parent):
    """jhkj"""
    for v in adj_list[u]:
        v = v[0]
        if state[v] == 'U':
            state[v] = 'D'
            parent[v] = u
            dfs_loop(adj_list, v, state, parent)
    state[u] = 'P'
def is_strongly_connected(adj_list):
    n = len(adj_list)
    found = True
    for i in range(n):
        s = dfs_tree(adj_list, i)
        for i in s:
            if i != 'P':
                found = False
                break
            else:
                found = True
    if found == True:
        return True
    else:
        return False

graph_string = """\
D 3
0 1
1 0
0 2
"""

print(is_strongly_connected(adjacency_list(graph_string)))