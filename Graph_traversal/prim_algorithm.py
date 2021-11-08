from math import inf
from adjacency_list import adjacency_list

# ----------------------------------------------------------------------------
def next_vertex(in_tree, distance):
    """kjhkj"""
    vertex = float('inf')
    indexs = 0
    for index, tree in enumerate(in_tree):
        if tree is False:
            if distance[index] <= vertex:
                vertex = distance[index]
                indexs = index
    return indexs
# ---------------------------------------------------------------------------

def prims(adj_list, s):
    """Prim's algorithm to find minimum spanning tree"""
    n = len(adj_list)
    in_tree = [False]*n
    distance = [float('inf')]*len(adj_list)    
    parent = [None]*n
    distance[s] = 0
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if in_tree[v] == False and weight < distance[v]:
                distance[v] = weight
                parent[v] = u
    return parent, distance
# -------------test1--------------------
graph_string = """\
U 7 W
0 1 5
0 2 7
0 3 12
1 2 9
2 3 4
1 4 7
2 4 4
2 5 3
3 5 7
4 5 2
4 6 5
5 6 2 
"""
print(prims(adjacency_list(graph_string), 0))
# -------------------------------------------------------------