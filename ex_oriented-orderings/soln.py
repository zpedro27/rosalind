import math
import itertools
import numpy as np


def calc_number_signed_permutations(n):
    """
    Each number in the set (or its symmetric) can be selected.
    Thus, the number of possible combinations is:
    (n*2) * ((n-1)*2) * ((n-2)*2) * (...)  = n! * 2^n
    """
    return (math.factorial(n)) * (2**n)


def get_all_signed_permutations(n):
    non_signed_permutations = itertools.permutations(range(1, n + 1))

    multipliers = generate_multipliers(n)

    output = None
    for non_signed in non_signed_permutations:
        signed_permutations = np.array(non_signed) * multipliers

        if output is None:
            output = signed_permutations
        else:
            output = np.append(output, signed_permutations, axis=0)

    return output


def generate_multipliers(n):
    """
    https://stackoverflow.com/questions/46255220/how-to-produce-permutations-with-replacement-in-python
    """
    choices = [-1, 1]
    repeats = [choices] * n
    out = list(itertools.product(*repeats))
    multipliers = np.array(out)
    return multipliers


def format_permutations(all_permutations):
    for permutation in all_permutations:
        print(" ".join([str(value) for value in permutation]))
    return


def save_to_file(filename, all_permutations):
    with open(filename, "w") as f:
        for permutation in all_permutations:
            f.write(" ".join([str(value) for value in permutation]) + "\n")
    return


def check_results(n, all_permutations):
    n_perm, n_elements = all_permutations.shape
    assert n_perm == calc_number_signed_permutations(n)


def main():
    n = 6
    out = calc_number_signed_permutations(n)
    print(out)

    all_perm = get_all_signed_permutations(n)
    # format_permutations(all_perm)
    check_results(n, all_perm)
    save_to_file("output_permutations.txt", all_perm)
    return


if __name__ == "__main__":
    main()
