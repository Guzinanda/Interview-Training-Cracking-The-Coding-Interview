"""
@   Binary Search

@   Problem
    Given a sorted array of nums 'nums' and a target value 'target', write a function to 
    search that target in nums. If target existm return its index, otherwise return -1.

@   Example
    Input:      nums = [-1,0,3,5,9,12]
                target = 9

    Output:     4

@   Template:
    01.

"""


def binarySearch(nums, target):

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = nums[mid]

        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return None


# TEST ___________________________________________________________________________________

# Example 01
nums = [-1,0,3,5,9,12]
target = 9
print(binarySearch(nums, target)) # 4

# Example 02
nums = [-1,0,3,5,9,12]
target = 2
print(binarySearch(nums, target)) # None
