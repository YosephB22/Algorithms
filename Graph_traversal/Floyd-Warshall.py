def adjacency_list(graph_string):
    header, *edges = [s.split() for s in graph_string.splitlines()]
    directed = header[0] == 'D' #directed is a boolean.
    weighted = len(header) == 3 and header[2] == 'W'
    num_vertices = int(header[1])
    adj_list = [[] for _ in range(num_vertices)] #[]*num_vertices
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

def distance_matrix(adj_list):
    """kjhkjhkj"""
    alist = []
    infinity = float('inf')
    matrix = [[0 for j in range(len(adj_list))]for i in range(len(adj_list))]
    for index, value in enumerate(adj_list):
        for n in adj_list[index]:
            edge = n[0]
            weight = n[1]
            matrix[index][edge] = n[1]
    for indexx, inf in enumerate(matrix):
        for v, g in enumerate(matrix[indexx]):
            if indexx != v:
                if g == 0:
                    matrix[indexx][v] = infinity
    return matrix

def floyd(distance):
    """finding the shortest path using floyd algorithm"""
    n = len(distance)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance

# -------test1-----------------
graph_str = """\
D 3 W
0 1 1
1 2 2
2 0 4
"""

adj_list = adjacency_list(graph_str)
dist_matrix = distance_matrix(adj_list)
print("Initial distance matrix:", dist_matrix)
dist_matrix = floyd(dist_matrix)
print("Shortest path distances:", dist_matrix)
# -----------------------------------------------
# ---------test2-----------------------------
graph_str = """\
D 3 W
0 1 1
1 2 2
2 0 4
"""

print(floyd(distance_matrix(adjacency_list(graph_str))))
# ---------------------------------------------------------