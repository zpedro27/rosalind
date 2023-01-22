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


def find_adjacency(sequences, k=3):

    for name, seq in sequences.items():
        v = name
        suffix = seq[-k:]
        # print(v, suffix)
        for name_, seq_ in sequences.items():
            if (seq_.startswith(suffix)) & (name_ != name):
                w = name_
                yield (v, w)


def display_results(adjacency):
    for (seq1, seq2) in adjacency:
        print(f"{seq1} {seq2}")


def test_adjacency():
    data = read_fasta("sample_data.txt")
    adj = find_adjacency(data)
    display_results(adj)   


if __name__ == "__main__":
    # test_adjacency()  # do not enable when generating output for the solution!....

    data = read_fasta("rosalind_grph.txt")
    adj = find_adjacency(data)
    display_results(adj)

