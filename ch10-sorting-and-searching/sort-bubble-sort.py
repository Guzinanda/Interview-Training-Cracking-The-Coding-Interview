"""
@   Sort Agorithm | Bubble Sort

@   Problem
    Given an unsorted array, sort it using Bubble Sort Algorithm.

@   Example
    Input:      list = [7,2,10,3,1]
    Output:     list = [1,2,3,7,10]

@   Explanation:
    https://www.youtube.com/watch?v=g_xesqdQqvA

"""

def bubbleSort(lis):
    
    indexing_lenght = len(lis) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, indexing_lenght):
            if lis[i] > lis[i+1]:
                sorted = False
                lis[i], lis[i+1] = lis[i+1], lis[i]
    
    return lis



# TEST _______________________________________________________________________     _____________________________________________________________________________________

lis = [7,2,10,3,1]
print(bubbleSort(lis))
