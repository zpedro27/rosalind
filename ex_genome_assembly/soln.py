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


def _matching_arms(matches, suffix, seq2, name1, name2):
    if (seq2.startswith(suffix)) & (name1 != name2):
        matches.append((name1, name2, len(suffix), len(seq2)))
    return matches


def find_adjacency(sequences): 
    """ 
    Adaptation of the function from the problem 'Overlapping graphs'.
    Returns pairs of overlapping sequences (maximum possible overlap length)
    """
    matches = []

    for name, seq in sequences.items():
        k = len(seq)
        stop = False

        while stop is False:
            n_edges_temp = len(matches)
            suffix = seq[-k:]

            for name_, seq_ in sequences.items():
                matches = _matching_arms(matches, suffix, seq_, name, name_)

            if len(matches) > n_edges_temp:
                stop = True
            else:
                k -= 1

    # print(matches)
    return matches


def _find_starting_sequence(sequences, adjacency):
    """ 
    Returns the Sequence from which the assembly will be built.
    This is the sequence for which the initial basepairs do NOT overlap
    with the suffix of any other sequence in the dataset.
    """
    all_seqs = set(sequences.keys())

    seqs_with_prefix = set([x[1] for x in adjacency])

    starting_seq, = all_seqs.difference(seqs_with_prefix)

    return starting_seq


def _find_next_sequence(adjacency, previous_seq):
    """ 
    Returns the next sequence to be used in the assembly.
    If multiple possibilities exist, the one with the longest overlap (with the 
    previous fragment) is chosen.
    """
    k_next = 0
    for values in adjacency:
        node1, node2, k, length = values

        if (node1 == previous_seq) & (k > k_next):
            k_next = k 
            next_seq = node2

    return next_seq, k_next


def find_superstring(sequences, adjacency):
    """ 
    Builds the genome assembly from the fragments.
    Assumes there is only one possible starting fragment.
    """

    starting = _find_starting_sequence(sequences, adjacency)

    sstring = sequences[starting]

    all_seqs = set(sequences.keys())
    used_seqs = set([starting])

    previous_seq = starting

    while used_seqs != all_seqs:
        next_seq, k_next = _find_next_sequence(adjacency, previous_seq)
        # print("All seqs:", all_seqs, "\n Used seqs: ", used_seqs)
        to_append = sequences[next_seq][k_next:]

        sstring += to_append

        used_seqs.add(next_seq)
        previous_seq = next_seq

    return sstring


def test_find_superstring():
    data = read_fasta("sample_data.txt")
    adj = find_adjacency(data)
    sstring = find_superstring(data, adj)
    assert sstring == "ATTAGACCTGCCGGAATAC"
    print("Test passed!")
    return


if __name__ == "__main__":
    # test_find_superstring()

    data = read_fasta("rosalind_long2.txt")
    adj = find_adjacency(data)
    sstring = find_superstring(data, adj)
    print(sstring)

    with open("output2.txt", "w") as f:
        f.write(sstring)

