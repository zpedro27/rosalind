# Calculating Expected Offspring

import numpy as np


def read_input(file):
    with open(file, "r") as f:
        x = f.readline().replace(" ", ",").replace("\n", "")

    x = [int(i) for i in x.split(",")]

    return np.array(x)


def expected_dominant_geno(x, offspring=2):
    """ 
    Input:
    x: number of couples with each of the geontype pairings (len = 6)
    offspring: number of offspring per couple

    Output:
    exp: expected number of offspring with the dominant allele
    """
    prob = np.array([1, 1, 1, 0.75, 0.5, 0])  # probability of the offspring carrying the dominant allele
    exp = np.sum(prob*x*offspring)
    return exp


def test_expected():
    x = np.array([1, 0, 0, 1, 0, 1])

    try:
        y = expected_dominant_geno(x)
        assert y == 3.5
        print("Test passed!")
    except:
        print("Test FAILED!")


if __name__ == "__main__":
    test_expected()

    x = read_input("rosalind_iev.txt")
    print("Input: ", x)
    print("Output:", expected_dominant_geno(x, offspring=2))