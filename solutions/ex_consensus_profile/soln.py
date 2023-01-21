import numpy as np


NUCLEOTIDE_ORDER = ["A", "C", "G", "T"]


def read_fasta(filename):
    data = {}
    with open(filename) as f:
        lines = f.readlines()
        for l in lines:
            if l[0] == ">":
                key = l[1:].replace("\n", "")
                data[key] = ""
            else:
                string = l
                data[key] += string.replace("\n", "")
    return data


def _determine_matrix_shape(data):
    data_lengths = {k: len(val) for k, val in data.items()}
    key_longest = max(data_lengths, key=data_lengths.get)

    n_cols = data_lengths[key_longest]
    n_rows = len(data_lengths)

    return (n_rows, n_cols)

def build_matrix(data):

    n_rows, n_cols = _determine_matrix_shape(data)
    matrix = []

    for i, (seq_name, seq) in enumerate(data.items()):
        vector = list(seq)
        matrix.append(vector)

    return np.array(matrix)


def _get_vector_from_counts_dict(x):
    return [val for k, val in x.items()]

def count_occurrences(matrix, nucl_order):

    ncols = matrix.shape[1]
    counts_all = []

    for i in range(ncols):
        counts_in_column = {n: 0 for n in nucl_order}

        column = matrix[:, i]
        counts_ = dict(zip(*np.unique(column, return_counts=True)))
        
        counts_in_column.update(counts_)

        counts_all.append(_get_vector_from_counts_dict(counts_in_column))

    return np.array(counts_all).T


def get_consensus(matrix_counts, nucl_order):

    consensus_indices = np.argmax(matrix_counts, axis=0)

    return "".join([nucl_order[i] for i in consensus_indices])


def main(filename, nucl_order):
    data = read_fasta(filename)
    mat = build_matrix(data)
    mat_counts = count_occurrences(mat, nucl_order)
    cons = get_consensus(mat_counts, nucl_order)
    np.savetxt("output.txt", mat_counts, fmt='%d')
    print(cons, mat_counts)
    return

def test_count_ocurrences():
    mat_counts_in = np.array([
                        [5, 1, 0, 0, 5, 5, 0, 0],
                        [0, 0, 1, 4, 2, 0, 6, 1],
                        [1, 1, 6, 3, 0, 1, 0, 0],
                        [1, 5, 0, 0, 0, 1, 1, 6]
        ])

    data = read_fasta("sample_data.txt")
    mat = build_matrix(data)
    mat_counts = count_occurrences(mat, NUCLEOTIDE_ORDER)

    assert np.array_equal(mat_counts, mat_counts_in) is True
    print("TEST count_occurrences: PASSED")
    return

def test_consensus():
    mat_counts = np.array([
                        [5, 1, 0, 0, 5, 5, 0, 0],
                        [0, 0, 1, 4, 2, 0, 6, 1],
                        [1, 1, 6, 3, 0, 1, 0, 0],
                        [1, 5, 0, 0, 0, 1, 1, 6]
        ])
    cons = get_consensus(mat_counts, NUCLEOTIDE_ORDER)

    assert cons == "ATGCAACT"
    print("TEST get_consensus: PASSED")
    return


if __name__ == "__main__":
    test_consensus()
    test_count_ocurrences()

    main("rosalind_cons.txt", NUCLEOTIDE_ORDER)

    # print(mat_counts)

    # print("argmax", np.argmax(mat_counts, axis=0))
    # print("max", np.max(mat_counts, axis=0))
    # print(get_consensus(mat_counts, NUCLEOTIDE_ORDER))
    # print(count_occurrences(mat))
    # print(np.array(["c", "d"], ["a", "b"], dtype=string_))