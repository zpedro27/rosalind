import numpy as np


def read_input(filename):
    with open(filename, "r") as f:
        lines = [line for line in f]
        seq = lines[0].strip("\n")

        A = np.array(lines[1].split(" ")).astype(float)
        print(seq, A)
    return seq, A


def probability_base(base, gc_content):
    """
    Determine the probability of observing a given base
    (assuming a given GC content).
    """
    p_gc = gc_content
    p_at = 1 - gc_content

    if base.lower() in ["a", "t"]:
        return p_at / 2
    elif base.lower() in ["g", "c"]:
        return p_gc / 2
    else:
        raise ValueError
        return


def probability(s, gc_content):
    """
    Calculate the probability of obtaining sequence s
    if each base is selected randomly assuming a given GC content.

    logP = log(p_base1) + log(p_base2) + ...
    """
    probability_each_base = np.array([probability_base(base, gc_content) for base in s])

    probability_each_base_log = np.log10(probability_each_base)

    return np.sum(probability_each_base_log)


def calc_random_string(s, A):
    B = np.array([])
    for gc_content in A:
        logp = probability(s, gc_content)
        B = np.append(B, logp)
    return np.round(B, 3)


def main():
    s, A = read_input("rosalind_prob.txt")
    b_out = calc_random_string(s, A)
    print(b_out)
    return


def test_random_string():
    seq, A = read_input("test_dataset.txt")
    b_out = calc_random_string(seq, A)

    print(b_out)
    B = np.array([-5.737, -5.217, -5.263, -5.360, -5.958, -6.628, -7.009])

    np.testing.assert_almost_equal(b_out, B)

    return


if __name__ == "__main__":
    print("test")
    test_random_string()
    print("")
    print("main")
    main()
