# Mortal Fibonacci Rabbits

import numpy as np


def read_inputs(file):
    """ 
    Parse the values of the arguments n and k from the provided .txt file
    """
    with open(file, "r") as f:
        n, k = f.readline().split()
    return int(n), int(k)


def mortal_rabbits(n, m, k=1):
    """

    """

    memory = np.zeros(m).astype(np.int64)   # it is important to ensure the integers are 64bit, otherwise will cause overflow...
    memory[1] = 1

    f_n2 = 1
    f_n1 = 1

    for i in range(2, n):
        
        offspring = k * (f_n2) 

        olds = memory[-1]

        memory = memory[0:-1]                # exclude the ones that die due to old age
        memory = np.insert(memory, 0, offspring) 
        
        f_n = f_n1 + offspring - olds

        f_n2 = f_n1 - olds
        f_n1 = f_n

    # # Alternative:
    # for i in range(2, n):

    #     offspring = k * np.sum(memory[1:])   # take all adults
    #     memory = memory[0:-1]                # exclude the ones that die due to old age
    #     memory = np.insert(memory, 0, offspring) 

    #     f_n = np.sum(memory)

        # print(i+1, f_n, memory)
    return np.int64(f_n)


def test_rabbits():
    try:
        f = mortal_rabbits(n=6, m=3, k=1)
        assert f == 4
        print("Test passed!")

    except Exception as e:
        print("FAILED")
        print(e)

    return


if __name__ == "__main__":
    test_rabbits()
    
    mortal_rabbits(n=6, m=4, k=1)
    n, m = read_inputs("rosalind_fibd.txt")
    print(f"Inputs: n={n}, m={m}")
    
    f = mortal_rabbits(n=n, m=m, k=1)
    print(f"After {n} months, there are {f} pairs")
    