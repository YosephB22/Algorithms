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

def transpose(adj_list):
    """
    takes the adjacency list of a graph and returns the 
    adjacency list of the reverse (transpose) of the graph
    """
    revresed_ad = [[] for _ in range(len(adj_list))]
    for index, value in enumerate(adj_list):
        for inner in value:
            inner_value = inner[0]
            revresed_ad[inner_value].append((index, inner[1]))
    return revresed_ad

graph_string = """\
D 3
0 1
1 0
0 2
"""

graph_adj_list = adjacency_list(graph_string)
graph_transposed_adj_list = transpose(graph_adj_list)
for i in range(len(graph_transposed_adj_list)):
    print(i, sorted(graph_transposed_adj_list[i]))