import re
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


def find_indices_character(s, char, start):
    all_occurrences = re.finditer(char, s)
    return [
        x.start() + start + 1 for x in all_occurrences
    ]  # +1 because the example assumes starting at 1


def find_all_indices(s, t):
    all_indices = []
    for i, char in enumerate(t):
        starting_index = i
        final_index = len(s) - len(t) + starting_index + 1
        indices = tuple(
            find_indices_character(s[starting_index:final_index], char, starting_index)
        )

        all_indices.append(indices)
        # print(i, char, indices)
    return all_indices


def isSequential(indices):
    ind = np.array(indices)

    if len(indices) == 0:
        return False
    else:
        index_diff = ind[1:] - ind[0:-1]
        return all(index_diff > 0)


def find_spliced_motifs(s, t):
    all_indices = find_all_indices(s, t)

    match = []
    counter = 0
    new_index = 0
    print(all_indices)

    while counter <= len(all_indices) - 1:
        to_select = np.array(all_indices[counter])

        try:
            new_index = np.min(to_select[to_select > new_index])
            print(new_index)
            match.append(new_index)
            counter += 1

        except IndexError:
            counter = 0
            match = []

        if isSequential(match) is False:
            counter = 0
            match = []

    return match


def main():
    data = read_fasta("rosalind_sseq.txt")

    keys = list(data.keys())

    s, t = data[keys[0]], data[keys[1]]

    match = find_spliced_motifs(s, t)

    match = [str(x) for x in match]
    print(" ".join(match))
    return


def test_spliced_motifs():
    data = read_fasta("test_dataset.txt")
    keys = list(data.keys())
    s, t = data[keys[0]], data[keys[1]]
    print(s, t)
    # assert (3, 8, 10) in
    print(find_spliced_motifs(s, t))
    return


if __name__ == "__main__":
    # test_spliced_motifs()
    main()
