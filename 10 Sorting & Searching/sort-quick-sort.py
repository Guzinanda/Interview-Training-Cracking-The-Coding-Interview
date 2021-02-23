"""
@   Sort Agorithm | Quick Sort

@   Problem
    Given an unsorted array of 'nums', write a function to Quick Sort them.

@   Example
    Input:      nums = [10,5,2,3]
    Output:     nums = [2,3,5,10]

"""

def quickSort(array):

    if len(array) < 2:                                                              # We check if the len of nums is 1
        return array                                                                # If it is just return the array, because one element arrays are already sorted [...]

    else:                                                                           # If it is greater we start our algorithm, we set a pivot and create two lists:
        pivot = array[0]                                                            # Pivot will be the firts element in the array.
        less = [i for i in array[1:] if i <= pivot]                                 # Our first list 'less', will be all the elements less than our pivot
        greater = [i for i in array[1:] if i > pivot]                               # Our second list 'greater', will be all the elements greater than our pivot [...]

        return quickSort(less) + [pivot] + quickSort(greater)                       # This is a recoursive algorithm, so we will return the function this wat:


# TEST _______________________________________________________________________     _____________________________________________________________________________________

nums = [10,5,2,3]
print(quickSort(nums))
