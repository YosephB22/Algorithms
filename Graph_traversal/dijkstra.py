
def adjacency_list(graph_string):
    header, *edges = [s.split() for s in graph_string.splitlines()]
    directed = header[0] == 'D' #directed is a boolean.
    weighted = len(header) == 3 and header[2] == 'W'
    num_vertices = int(header[1])
    adj_list = []
    for i in range(num_vertices):#[]*num_vertices
        adj_list.append([])
    for edge in edges:
        edge_data = map(int, edge)
        if weighted:
            source, target, weight = edge_data
        else:
            source, target = edge_data
            weight = None
        adj_list[source].append((target, weight))
        if not directed:
            adj_list[target].append((source, weight))
    return adj_list
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
def dijkstra(adj_list, start):
    n = len(adj_list)
    intree = [False] * n
    infi = float('inf')
    distance = [infi] * n
    parent = [None] * n
    distance[start] = 0
    while not all(intree): # while not all of the vertices are nor part of the tree
        u = next_vertex(intree, distance)
        intree[u] = True
        for v, weight in adj_list[u]:
            if not intree[v] and (distance[u] + weight < distance[v]):
                distance[v] = distance[u] + weight
                parent[v] = u
    return parent, distance

graph_string = """\
D 3 W
1 0 3
2 0 1
1 2 1
"""

print(dijkstra(adjacency_list(graph_string), 1))
print(dijkstra(adjacency_list(graph_string), 2))