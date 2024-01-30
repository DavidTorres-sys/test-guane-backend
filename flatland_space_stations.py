#!/bin/python3
import os

# Complete the flatlandSpaceStations function below.

def flatlandSpaceStations(n, c):
    #Firts wee sort the array of the cities
    #with space statios
    c.sort()
    #We initialize the max distance to the first city
    max_distance = 0
    max_distance = max(max_distance, c[0])
    for i in range(1, len(c)):
        # Calculate distance between two adjacent cities
        distance = (c[i] - c[i-1]) // 2
        max_distance = max(max_distance, distance)
    return max(max_distance, n - 1 - c[-1])
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
 