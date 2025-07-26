from typing import List

# Find the longest chain of consecutive numbers in an array. Two numbers are consecutive if
# they have a difference of 1.
# Example:
# Input: nums = [1, 6, 2, 5, 8, 7, 10, 3]
# Output: 4
# Explanation: The longest chain of consecutive numbers is 5, 6, 7, 8.
# Time and space O(N)
def longest_chain_of_consecutive_numbers(nums: List[int]) -> int:
    if not nums:
        return 0
    num_set = set(nums)
    longest_chain = 0
    for num in num_set:
        # If the current number is the smallest number in its chain, search for
        # the length of its chain.
        if num - 1 not in num_set:
            current_num = num
            current_chain = 1
            # Continue to find the next consecutive numbers in the chain.
            while current_num + 1 in num_set:
                current_num += 1
                current_chain += 1
            longest_chain = max(longest_chain, current_chain)
            
    return longest_chain