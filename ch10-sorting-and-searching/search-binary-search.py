"""
@   Search Agorithm | Binary Search

@   Problem
    Given a sorted array 'nums' and a target value 'target', write a function to search 
    that target in nums. If target existm return its index, otherwise return -1.

@   Example
    Input:      nums = [-1,0,3,5,9,12]
                target = 9
    Output:     4

"""

def binarySearch(nums, target):                                                     # This only works for sorted elements.

    low = 0                                                                         # We set a 'low' variable of 0
    high = len(nums) - 1                                                            # We set a 'high' variable that will be the len of our 'nums' - 1 
                                                                                    # These will be our firts position and last position [...]

    while low <= high:                                                              # We create a while loop that chechs if we still have a range
        mid = (low + high) // 2                                                     # We set a 'mid' variable what will be the floor division of 'low' + 'high'
        guess = nums[mid]                                                           # We set a 'guess' variable what is the middle of our range [...]

        if guess == target:                                                         # If the value we took 'guess' is == to our target     
            return mid                                                              # We already found the number, so retur that 'mid'.

        elif guess > target:                                                        # If the value we took 'guess' is > (greater) to our target    
            high = mid - 1                                                          
        else:                                                                       # If the value we took 'guess' is < (lesser) to our target    
            low = mid + 1
    
    return None


# TEST _______________________________________________________________________     _____________________________________________________________________________________

# Example 01
nums = [-1,0,3,5,9,12]
target = 9
print(binarySearch(nums, target)) # 4

# Example 02
nums = [-1,0,3,5,9,12]
target = 2
print(binarySearch(nums, target)) # None
