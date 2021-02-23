"""
@   Sort Agorithm | Merge Sort

@   Problem
    Given an unsorted array, sort it using Merge Sort Algorithm.

@   Example
    Input:      list = [7,2,10,3,1]
    Output:     list = [1,2,3,7,10]

@   Explanation:
    https://www.youtube.com/watch?v=_trEkEX_-2Q

"""

def mergeSort(lis):
    
    if len(lis) > 1:
        mid = len(lis) // 2
        left_lis = lis[:mid]
        right_lis = lis[mid:]

        mergeSort(left_lis)
        mergeSort(right_lis)

        i = 0
        j = 0
        k = 0

        while i < len(left_lis) and j < len(right_lis):
            if left_lis[i] < right_lis[j]:
                lis[k] = left_lis[i]
                i = i + 1
                k = k + 1
            else:
                lis[k] = right_lis[j]
                j = j + 1
                k = k + 1

        while i < len(left_lis):
            lis[k] = left_lis[i]
            i = i + 1
            k = k + 1

        while j < len(right_lis):
            lis[k] = right_lis[j]
            j = j + 1
            k = k + 1

    return lis


# TEST _______________________________________________________________________     _____________________________________________________________________________________

lis = [7,2,10,3,1]
print(mergeSort(lis))
