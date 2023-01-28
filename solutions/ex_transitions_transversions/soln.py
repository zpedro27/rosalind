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


def get_seqs_from_dict(data):
    return [val for _, val in data.items()]


def find_differences(seq1, seq2):
    """ 
    Finds the locations where the bases in the two strains differ.
    """
    s1 = np.array(list(seq1))
    s2 = np.array(list(seq2))
    indices_diff = s1 != s2
    return s1[indices_diff], s2[indices_diff]


def get_base_type(seq):
    """ 
    Return the sequences where each base has been replaced by its type
    Purine: X
    Pyrimidine: Y
    """
    seq[(seq == "G") | (seq == "A")] = "X"
    seq[(seq == "C") | (seq == "T")] = "Y"
    return seq


def calc_R(seq1, seq2):
    """ 
    Transitions: C <-> T and A <-> G (i.e. purine-purine and pyrimidine-pyrimidine)

    Transversions: e.g. C <-> A, ... (i.e. purine-pyrimidine)
"""
    transitions = np.sum(seq1 == seq2)
    transversions = np.sum(seq1 != seq2)
    return transitions/transversions


def main():
    data = read_fasta("rosalind_tran.txt")
    seq1, seq2 = get_seqs_from_dict(data)
    s1, s2 = find_differences(seq1, seq2)

    s1_ = get_base_type(s1)
    s2_ = get_base_type(s2) 

    print("R(s1, s2): ", calc_R(s1_, s2_))  
    return


def test_main():
    seq1 = "GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT"
    seq2 = "TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT"

    s1, s2 = find_differences(seq1, seq2)

    s1_ = get_base_type(s1)
    s2_ = get_base_type(s2)

    assert np.isclose(calc_R(s1_, s2_), 1.21428571429)
    print("Passed!")


if __name__ == "__main__":
    # test_main()
    main()