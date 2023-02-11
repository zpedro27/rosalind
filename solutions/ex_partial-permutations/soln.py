import math


def read_inputs(file):
    """
    Parse the values of the arguments n and k from the provided .txt file
    """
    with open(file, "r") as f:
        n, k = f.readline().split()
    return int(n), int(k)


def partial_permutations(n, k):
    no_combinations = math.comb(n, k)  # computes nCr(n, k)

    no_permutations_subset = math.factorial(k)  # computes k!

    partial_permutations = no_combinations * no_permutations_subset

    return partial_permutations % 1000000


def test_partial_permutations():
    n = 21
    k = 7
    assert partial_permutations(n, k) == 51200


def main():
    n, k = read_inputs("rosalind_pper.txt")
    output = partial_permutations(n, k)

    print(n, k)
    print(output)
    return


if __name__ == "__main__":
    test_partial_permutations()
    main()
