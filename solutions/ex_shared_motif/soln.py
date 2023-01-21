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


def find_shortest_sequence(data):

    length_seq = {k: len(seq) for k, seq in data.items()}

    key_shortest = min(length_seq, key=length_seq.get)
    len_shortest = length_seq[key_shortest]

    return key_shortest, len_shortest


def check_substring_all_sequences(sequences, substring):

    present_in_all = True

    for seq_name, seq in sequences.items():
        is_present = substring in seq
        present_in_all = present_in_all * is_present

    return bool(present_in_all)


def find_motif(sequences: dict):
    key_shortest, len_shortest = find_shortest_sequence(sequences)
    seq_shortest = sequences[key_shortest]

    window = len_shortest
    stop = False
    temp_stop = False

    while stop is False:
        for i in range(0, len_shortest-window+1):
            substring = seq_shortest[i:i+window]

            present_in_all = check_substring_all_sequences(sequences, substring)

            if present_in_all is True:
                yield substring
                temp_stop = True  # no need to keep on searching for shorter substrings

        if temp_stop is True:
            stop = True
        else:
            window -= 1


def test_find_motif():
    print("TEST")
    data = read_fasta("sample_data.fasta")
    motif = find_motif(data)
    print(list(motif))
    # assert motif == "AC"
    return


if __name__ == "__main__":
    test_find_motif()

    data = read_fasta("rosalind_lcsm.txt")
    motif = find_motif(data)

    print("All longest common substrings: ", list(motif))
