# Rabbits and Recurrence Relations

def read_inputs(file):
    """ 
    Parse the values of the arguments n and k from the provided .txt file
    """
    with open(file, "r") as f:
        n, k = f.readline().split()
    return int(n), int(k)


def rabbits(n, k):
    """
    Computes the n-th value of the Fibonnaci sequence. On each iteration, 
    a certain number of offspring is added to the population. This offspring 
    is only produced by the pairs in reproductive-age (two months old, 
    i.e. f_n-2).
    
    Note: does not work with storing all the values in an array, as it will 
    encounter an error of overflow due to the long scalar values.

    Input:
    n: number of months
    k: number of rabbit PAIRS as offspring

    Output:
    f_n: number of rabbit pairs after n months
    """

    f_n1 = 1
    f_n2 = 1

    for i in range(2, n):
        # f[i] = f[i-1] + k*f[i-2]  
        # only-reproductive-age rabbits (2 months old) generate offspring

        f_n = f_n1 + k*f_n2

        f_n2 = f_n1
        f_n1 = f_n

    return f_n


def test_rabbits():
    try:
        f = rabbits(n=5, k=3)
        assert f == 19
        print("Test passed!")

    except Exception as e:
        print("FAILED")
        print(e)

    return


if __name__ == "__main__":
    test_rabbits()
    
    n, k = read_inputs("rosalind_fib.txt")
    print(f"Inputs: n={n}, k={k}")
    
    f = rabbits(n, k)
    print(f"After {n} months, there are {f} pairs")
    