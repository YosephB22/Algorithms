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
print(adjacency_list(graph_string))
print(adjacency_list(graph_string))