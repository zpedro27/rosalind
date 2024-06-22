import numpy as np


def read_input(filename):
    """
    Parse the values of the arguments n and edge list from the provided .txt file
    """
    counter = 0
    edge_list = []

    with open(filename, "r") as f:
        for line in f:
            if counter == 0:
                n = line.strip("\n")
                n = int(n)
                counter += 1
            else:
                node1, node2 = line.strip("\n").split()
                edge_list.append((int(node1), int(node2)))
    return n, edge_list


def construct_adjacency_matrix(n, edge_list):
    """
    Construct an adjacency matrix from a list of edges.
    The diagonal elements are set to 0.
    """
    matrix = np.zeros((n, n))

    for edge in edge_list:
        i, j = edge

        # # Populate the diagonal:
        # matrix[i - 1, i - 1] = 1
        # matrix[j - 1, j - 1] = 1

        # Populate connections between nodes:
        matrix[i - 1, j - 1] = 1
        matrix[j - 1, i - 1] = 1

    return matrix


def find_disconnected_components(adjacency_matrix):
    """
    Recursively traverse the nodes in a graph,
    returning the (number of) sets of connected nodes.
    """
    no_components = 0
    no_nodes = len(adjacency_matrix)

    all_seen_nodes = set()
    remaining_nodes = set(range(no_nodes))

    while remaining_nodes != set():
        node = remaining_nodes.pop()

        nodes_seen_ = recursive_graph_traversal(node, adjacency_matrix)

        all_seen_nodes.update(nodes_seen_)
        remaining_nodes = remaining_nodes - nodes_seen_

        no_components += 1

        # print(f"Starting from node {node} --> connected to: {nodes_seen_}")
        # print(
        #     f"All nodes seen so far: {all_seen_nodes}. Nodes left to explore: {remaining_nodes}"
        # )
        # print(f"This is component no. {no_components}")
        # print("")

    return no_components


def recursive_graph_traversal(node, adjacency_matrix, elements_comp=set()):
    # Duplicate the input set of component nodes to prevent inplace modification:
    elements_in_component = elements_comp.copy()

    # Find all nodes connected to the selected node:
    node_connectivity = adjacency_matrix[node, :]
    (other_nodes,) = np.where(node_connectivity > 0)
    other_nodes = set(other_nodes)

    # Break if the new nodes have already been visited
    if other_nodes.issubset(elements_in_component):
        return elements_in_component

    # Add new nodes to the set of nodes connected:
    elements_in_component.update(other_nodes)

    # Make copy so that one doens't .pop() from the set of connected elements
    elements_copy = elements_in_component.copy()

    node_new = int(elements_copy.pop())

    return recursive_graph_traversal(node_new, adjacency_matrix, elements_in_component)


def compute_minimal_number_edges_needed(adjacency_matrix):
    no_disconnected_components = find_disconnected_components(adjacency_matrix)

    return no_disconnected_components - 1


def alternative_solution(n, edge_list):
    return n - len(edge_list) - 1


def test_tree():
    n, edges = read_input("example_dataset.txt")
    mat = construct_adjacency_matrix(n, edges)
    edges_needed = compute_minimal_number_edges_needed(mat)
    assert edges_needed == 3
    print("TEST PASSED!")


def main(filename):
    n, edges = read_input(filename)
    mat = construct_adjacency_matrix(n, edges)
    print(mat.shape)
    edges_needed = compute_minimal_number_edges_needed(mat)
    print(edges_needed)

    print("alternative: ", alternative_solution(n, edges))
    return


if __name__ == "__main__":
    test_tree()
    main("rosalind_tree.txt")
