def connected_components(list_of_nodes):
    connected_nodes = {}
    for node in list_of_nodes:
        if node.label not in connected_nodes:
            connected_nodes[node.label] = []
        for key in connected_nodes:
            if node.label == key:
                connected_nodes[key].append(node)
    return connected_nodes # returns a dictionary where key = label and the values are lists of the nodes