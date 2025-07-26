from typing import List

# Given an array of integers, modify the array in place to move all zeros to the end while
# maintaining the relative order of non-zero elements.
# Example: Input: nums = [0, 1, 0, 3, 2], Output: [1, 3, 2, 0, 0]
def shift_zeros_to_the_end(nums: List[int]) -> None:
    # The 'left' pointer is used to position non-zero elements.
    left = 0
    # Iterate through the array using a 'right' pointer to locate non-zero 
    # elements.
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            # Increment 'left' since it now points to a position already occupied 
            # by a non-zero element.
            left += 1
