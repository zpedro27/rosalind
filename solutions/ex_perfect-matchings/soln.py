import math
import collections


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


def count_bases(seq):
    return collections.Counter(seq)


def count_perfect_matchings(seq):
    counts = count_bases(seq)

    no_AU_pairs = counts["A"]  # there are as many A's as U's'
    no_GC_pairs = counts["G"]  # same for G's and C's

    no_matchings_AU = math.factorial(no_AU_pairs)
    no_matchings_GC = math.factorial(no_GC_pairs)

    return no_matchings_AU * no_matchings_GC


def test_perfect_matchings():
    seq_dict = read_fasta("testdataset.fasta")
    keys = list(seq_dict.keys())

    seq = seq_dict[keys[0]]
    assert count_perfect_matchings(seq) == 12

    return


def main():
    seq_dict = read_fasta(".fasta")
    keys = list(seq_dict.keys())

    seq = seq_dict[keys[0]]
    print(count_perfect_matchings(seq))
    return


if __name__ == "__main__":
    test_perfect_matchings()
    main()
