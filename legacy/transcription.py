def dna_to_rna(base):
    if base.lower() == "t":
        return "U"
    elif base.lower() in ["a", "c", "g"]:
        return base
    else:
        return ""

def transcribe_strand(s):
    t = [dna_to_rna(base) for base in s]
    return "".join(t)

f = open("rosalind_rna.txt", "r")
a = f.read()
transcribe_strand(a)