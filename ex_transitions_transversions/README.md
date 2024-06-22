# Transitions and Transversions

## Problem
For DNA strings `s1` and `s2` having the same length, their transition/transversion ratio `R(s1,s2)` is the ratio of the total number of transitions to the total number of transversions, where symbol substitutions are inferred from mismatched corresponding symbols as when calculating Hamming distance (see “Counting Point Mutations”).

*Given*: Two DNA strings `s1` and `s2`  of equal length (at most 1 kbp).

*Return*: The transition/transversion ratio `R(s1,s2)`.


## Example

### Sample Dataset
```
>Rosalind_0209

GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT

>Rosalind_2200

TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT
```

### Sample Output
`1.21428571429`