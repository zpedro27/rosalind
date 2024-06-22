import numpy as np


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


def construct_distance_matrix(data):
    n_sequences = len(data)

    data_renamed_seqs = {i: seq for i, (_, seq) in enumerate(data.items())}

    D_matrix = np.zeros((n_sequences, n_sequences))

    # Populate just the upper part of the matrix:
    for i in range(n_sequences):
        for j in range(i, n_sequences):
            seq1 = data_renamed_seqs[i]
            seq2 = data_renamed_seqs[j]
            D_matrix[i, j] = calc_distance_sequences(seq1, seq2)

    # Reflect triangular matrix:
    D_matrix = D_matrix + D_matrix.T - np.diag(np.diag(D_matrix))

    return np.around(D_matrix, decimals=5)


def calc_distance_sequences(s1, s2):
    seq1_array = np.array(list(s1))
    seq2_array = np.array(list(s2))

    matches = seq1_array == seq2_array
    matches = matches.astype(int)

    similarity = matches.mean()

    return 1 - similarity


def test_distance():
    data = read_fasta("example_dataset.txt")
    D = construct_distance_matrix(data)

    expected = np.array(
        [
            [0.00000, 0.40000, 0.10000, 0.10000],
            [0.40000, 0.00000, 0.40000, 0.30000],
            [0.10000, 0.40000, 0.00000, 0.20000],
            [0.10000, 0.30000, 0.20000, 0.00000],
        ]
    )
    assert np.allclose(expected, D)
    print("TEST PASSED!")
    return


def main(filename):
    data = read_fasta(filename)
    D = construct_distance_matrix(data)
    # np.set_printoptions(precision=5)
    # for i in range(len(D)):
    #     print(D[i, :])
    return


if __name__ == "__main__":
    test_distance()
    main("rosalind_pdst.txt")
