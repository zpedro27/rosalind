# Legacy

import random


PAIRS = {"A": "U", "G": "C", "C": "G", "U": "A"}


def _label_bases(seq):
    return [x + "_" + str(i) for i, x in enumerate(seq)]


def get_adjacency_edges(seq):
    edges = []
    labeled_seq = _label_bases(seq)
    for i, base in enumerate(labeled_seq[:-1]):
        edges += [(base, labeled_seq[i + 1])]
    return edges


def get_basepair_edges(seq):
    edges = []

    labeled_seq = _label_bases(seq)

    for i, base in enumerate(labeled_seq):
        b = base.split("_")[0]
        edge_bp = [
            (base, base2)
            for base2 in labeled_seq[i + 1 :]
            if base2.startswith(PAIRS[b])
        ]
        edges += edge_bp

    return edges


def update_edges(edges, nodes_used):
    return [
        pair
        for pair in edges
        if (pair[0] not in nodes_used) and (pair[1] not in nodes_used)
    ]


def get_matching(edges):
    nodes_used = []
    edges_to_use = edges
    matching = []
    counter = 0

    for i in range(edges):
        while len(edges_to_use) > 0:
            new_edge = random.choice(edges_to_use)

            node1, node2 = new_edge
            nodes_used.append(node1)
            nodes_used.append(node2)

            matching += [new_edge]

            edges_to_use = update_edges(edges_to_use, nodes_used)

            print(counter, edges_to_use)
            counter += 1

            new_edge = edges_to_use[0]

    return matching


def is_perfect(matching, no_nodes):
    if len(matching) == no_nodes / 2:
        return True
    return False
