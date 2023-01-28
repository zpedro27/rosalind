import regex as re
import requests


def read_input_ids(filename):
    uniprotIDs = []
    with open(filename, "r") as f:
        for line in f:
            id_ = line.strip("\n").split("_")[0]  # get only the primary accession key
            uniprotIDs.append(id_)
    return uniprotIDs    


def get_protein_url(uniprotID):
    return f"http://www.uniprot.org/uniprot/{uniprotID}.fasta"


def download_fasta_from_uniprot(uniprotIDs, outputfilename):
    for protID in uniprotIDs:
        url = get_protein_url(protID)
        r = requests.get(url, allow_redirects=True)

        with open(outputfilename, "ab") as f:
            f.write(r.content)
    return


def read_fasta(filename):
    data = {}
    with open(filename) as f:
        lines = f.readlines()
        for l in lines:
            if l[0] == ">":
                key = l[1:].replace("\n", "").split("|")[1]
                data[key] = ""
            else:
                string = l
                data[key] += string.replace("\n", "")
    return data


def find_motif(sequences, pattern):
    for name, seq in sequences.items():
        print(name)
        matching_indices = [str(m.start()+1) for m in re.finditer(pattern, seq, overlapped=True)]  # it is important to find all possible instances of the motif, even if overlapping!
        print(" ".join(matching_indices))
    return


def main():

    glycosylation_motif = r"N[^P][ST][^P]"  # see https://regex101.com/
    # Glycosylation motif: N{P}[ST]{P}. 
    # where:
    # [XY] means "either X or Y"
    # {X} means "any amino acid except X."

    ids = read_input_ids("rosalind_mprt.txt")
    print("protein IDS", ids)

    download_fasta_from_uniprot(ids, "protein_data.txt")
    data = read_fasta("protein_data.txt")
    find_motif(data, glycosylation_motif)


if __name__ == "__main__":
    main()