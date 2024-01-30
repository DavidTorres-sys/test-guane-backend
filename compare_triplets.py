#!/bin/python3
import os
#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def compareTriplets(a, b):
    #iterate over the elements in the same position in the arrays a and b
    #and compare them if a[i] > b[i] then alice gets a point, if b[i] > a[i] then
    #bob gets a point.
    return sum(1 for i, j in zip(a, b) if i > j), sum(1 for i, j in zip(a, b) if j > i)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
