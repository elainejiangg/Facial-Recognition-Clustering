import random

def propagate_label(node, neighbors, adjacency_matrix):
    # neighbors should be an iterable
    # returns nothing, just updates in place
    edge_weights = {}
    for neighbor in neighbors:
        if neighbor.label not in edge_weights:
            edge_weights[neighbor.label] = 0
        edge_weights[neighbor.label] += adjacency_matrix[node.id][neighbor.id]

    if edge_weights:
        node.label = max(edge_weights, key=edge_weights.get)