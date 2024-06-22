""" 
Since A and B are independent alleles, we can just focus on what happens with one of them.
P(AaBb) = P(Aa) * P(Bb) = P(Aa) * P(Aa)

Possible matchings with a Aa individual:
1. Aa x Aa:
    AA; Aa; aA; aA --> P(Aa) = 0.5

2. AA x Aa:
    AA; AA; Aa; Aa --> P(Aa) = 0.5

3. aa x Aa:
    aA; aa; aA; aa --> P(Aa) = 0.5

"""
import math


def calc_number_individuals(k):
    return 2**k


def calc_probability_exactly_heterozygotic(no_individuals_generation, N):

    c = math.comb(no_individuals_generation, N)

    # no_cases_homozygotic = (
    #     (c / no_individuals_generation)
    #     * ((0.5) ** N)
    #     * (0.5 ** (no_individuals_generation - N))
    # )

    return 0.5**no_individuals_generation


def main(k, N):
    no_individuals_generation = calc_number_individuals(k)

    p = 0
    for n in range(N, no_individuals_generation + 1):
        print(n)

        p_ = calc_probability_exactly_heterozygotic(no_individuals_generation, n)

        print(f"probability exactly {n} are heterozygotic: {p_**2}")
        p += p_**2

    print(f"probability at least {N} heterozygotic: {p}")
    p_Aa = p  # 1 - p

    p_AaBb = p_Aa * p_Aa

    print(p_AaBb)
    return


if __name__ == "__main__":
    main(k=2, N=1)
