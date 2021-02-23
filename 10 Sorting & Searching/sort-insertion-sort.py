"""
@   Sort Agorithm | Merge Sort

@   Problem
    Given an unsorted array, sort it using Insertion Sort Algorithm.

@   Example
    Input:      lis = [7,2,10,3,1]
    Output:     lis = [1,2,3,7,10]

@   Explanation:
    https://www.youtube.com/watch?v=lEA31vHiry4

"""

def insertionSort(lis):
    
    for index in range(1, len(lis)):
        value = lis[index]
        i = index -1
        
        while i >= 0:
            if value < lis[i]:
                lis[i + 1] = lis[i]                                                  # Shift number in solt i right to slot i+1
                lis[i] = value                                                       # Shift value left into slot i
                i = i - 1
            else:
                break
    
    return lis



# TEST _______________________________________________________________________     _____________________________________________________________________________________

lis = [5,8,4,9,6]
print(insertionSort(lis))
