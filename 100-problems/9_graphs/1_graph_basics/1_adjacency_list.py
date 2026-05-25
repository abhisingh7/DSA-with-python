# Write a Python function that:

# Takes a list of edges as input — like [[1,2], [1,3], [2,4], [3,4]]
# Builds and returns an adjacency list (dictionary) for an undirected graph

from collections import defaultdict

def adjacency_list(edges, directed=False):
    adj_dict = defaultdict(list)  # Created ONCE, outside loop

    for edge in edges:
        node1 = edge[0]
        node2 = edge[1]

        # add node2 to node1's list
        adj_dict[node1].append(node2)
        # AND add node1 to node2's list (undirected!)
        if not directed:
            adj_dict[node2].append(node1)

    return adj_dict

# Test
mylist = [[1,2], [1,3], [2,4], [3,4]]

print(adjacency_list(mylist)) # Undirected Graph

print(adjacency_list(mylist, True)) # Directed Graph