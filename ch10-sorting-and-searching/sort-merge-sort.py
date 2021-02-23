"""
@   Sort Agorithm | Merge Sort

@   Problem
    Given two sorted integer arrays nums1 and nums2, merge them.

@   Example
    Input:      nums1 = [1,2,3,0,0,0]
                nums2 = [2,5,6]
                m = 3
                n = 3

    Output:     nums1 = [1,2,2,3,5,6]

"""

def mergeSort(nums1, m, nums2, n):

    nums1_copy = nums1[:m]                                                          # We make a copy of the first 'm' elements of 'nums1'

    p1 = 0                                                                          # We create read pointers for nums1_copy and nums2 respectively.
    p2 = 0

    for i in range(m + n):                                                          
        if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
            nums1[i] = nums1_copy[p1]
            p1 += 1

        else:
            nums1[i] = nums2[p2]
            p2 += 1

    return nums1


# TEST _______________________________________________________________________     _____________________________________________________________________________________

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

print(mergeSort(nums1, m, nums2, n))
