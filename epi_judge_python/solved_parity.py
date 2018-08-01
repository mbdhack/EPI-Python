from test_framework import generic_test


def parity(x):
    # TODO - you fill in here.
    result = 0
    while x:
        result ^= 1 #1 or 0 toggle based on what 
        x &= (x-1) #drop lowest set bit
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
