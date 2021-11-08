def adjacency_matrix(graph_str):
    """constructing a matrix"""
    header, *edges = [edge.split() for edge in graph_str.splitlines()]
    n = int(header[1])
    matrix_for_d = [[None] * n for _ in range(n)]
    matrix_for_u = [[0] * n for _ in range(n)]
    for edge in edges:
        u = int(edge[0])
        v = int(edge[1])
        if len(edge) == 3:
            weight =  int(edge[2])
            directed = (header[0]) == 'D'
            if directed:
                matrix_for_d[u][v] = (weight)
            else:
                matrix_for_d[u][v] = (weight)
                matrix_for_d[v][u] = (weight)
        else:
            directed = (header[0]) == 'D'
            if directed:
                matrix_for_u[u][v] = 1
            else:
                matrix_for_u[u][v] = 1
                matrix_for_u[v][u] = 1
    if len(header) == 3:
        return matrix_for_d
    else:
        return matrix_for_u


graph_string = """\
D 3 W
0 1 7
1 0 -2
0 2 0
"""
graph_string = """\
D 3
0 1
1 0
0 2
"""

print(adjacency_matrix(graph_string))

print(adjacency_matrix(graph_string))