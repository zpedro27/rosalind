import regex as re


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


def read_codon_table(filename):
    f = open(filename, "r")
    a = f.readlines()

    codon_table = {}
    for line in a:
        (parsed_line,) = line.replace("\n", "").replace(" ", "").split(" ")
        no_matches = int(len(parsed_line) / 4)

        for i in range(no_matches):
            section = parsed_line[4 * i : 4 * (i + 1)]
            codon = section[0:3]
            aa = section[-1]

            codon = codon.replace("U", "T")  # to translate directly from DNA
            codon_table[codon] = aa
    return codon_table


def get_aa(codon, codon_table):
    return codon_table[codon]


def reverse_complement(sequence):
    complementary_base = {"A": "T", "C": "G", "G": "C", "T": "A"}

    reverse_seq = sequence[::-1]

    complementary_seq = [complementary_base[b] for b in reverse_seq]

    return "".join(complementary_seq)


def translate_strand(sequence, codon_table):
    n = len(sequence)

    remainder = n % 3

    n_codons = int((n - remainder) / 3)

    protein = ""
    for i in range(n_codons):
        codon = sequence[3 * i : 3 * (i + 1)]
        aa = get_aa(codon, codon_table)
        protein += aa

    return protein


def append_orfs(all_orfs, new_matches):
    for match in new_matches:
        if (len(match) > 0) & (match not in all_orfs):
            all_orfs.append(match)
    return


def find_orfs(sequence, codon_table):
    rev_sequence = reverse_complement(sequence)

    all_orfs = []

    sequences_to_translate = [sequence, rev_sequence]

    for seq in sequences_to_translate:
        for starting_index in range(3):
            aa_sequence = translate_strand(seq[starting_index:], codon_table)
            # print(seq, " -->  ", starting_index, " -->  ", aa_sequence)

            matches = re.findall(r"(M\w*)\*", aa_sequence, overlapped=True)

            append_orfs(all_orfs, matches)

    return all_orfs


def main():
    codon_table = read_codon_table("codon_table.txt")

    data = read_fasta("rosalind_orf.txt")
    sequence = list(data.values())[0]

    ORFs = find_orfs(sequence, codon_table)

    for x in ORFs:
        print(x)
    return


if __name__ == "__main__":
    main()
