# Genome Assembly as Shortest Superstring

## Problem
For a collection of strings, a larger string containing every one of the smaller strings as a substring is called a superstring.

By the assumption of parsimony, a shortest possible superstring over a collection of reads serves as a candidate chromosome.

*Given*: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

*Return*: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).


## Example
*Sample Dataset*:

```>Rosalind_56
ATTAGACCTG

>Rosalind_57
CCTGCCGGAA

>Rosalind_58
AGACCTGCCG

>Rosalind_59
GCCGGAATAC```


*Sample Output*: 

ATTAGACCTGCCGGAATAC