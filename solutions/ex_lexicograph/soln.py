import itertools


def read_input(filename):
    with open(filename, "r") as f:
        lines = [line.strip("\n") for line in f.readlines()]

        alphabet = lines[0].split(" ")
        n = int(lines[1])

    return alphabet, n


def find_all_combinations(alphabet, n):
    repeats = [alphabet] * n
    return list(
        itertools.permutations(alphabet, n)
    )  # list(itertools.product(*repeats))  #


def sort_combinations(all_combination):
    output = []
    for combination in all_combination:
        combination_list = list(combination)
        sorted_combination = sorted(combination_list)

        output.append("".join(sorted_combination))
    return output


def main():
    alphabet, n = read_input("test_dataset.txt")

    all_combinations = find_all_combinations(alphabet, n)
    print(list(all_combinations))

    output = sort_combinations(all_combinations)

    # for x in output:
    #     print(x)
    return


if __name__ == "__main__":
    main()
    read_input("test_dataset.txt")
