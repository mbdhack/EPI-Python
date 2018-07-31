from test_framework import generic_test


def plus_one(A):
    A[-1] += 1 # add one to the last element of A

    for i in reversed(range(1,len(A))):
        if A[i] != 10: # the last element was not 9(max)
            break
        # there is a carry
        #set the digit to zero and add the carry to the digit before it
        A[i] =0
        A[i-1] += 1
    # if the first digit is 10, a cary was applied
    #set it to one and add 0.
    if A[0] == 10:
        A[0]=1
        A.append(0)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
