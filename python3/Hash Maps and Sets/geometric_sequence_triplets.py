from collections import defaultdict
from typing import List


# A geometric sequence triplet is a sequence of three numbers where each successive number is
# obtained by multiplying the preceding number by a constant called the common ratio.
# Let's examine three triplets to understand how this works:
# ● (1, 2, 4): Geometric sequence with a ratio of 2 (i.e., [1, 1·2 = 2, 2·2 = 4]).
# ● (5, 15, 45): Geometric sequence with a ratio of 3 (i.e., [5, 5·3 = 15, 15·3 = 45]).
# ● (2, 3, 4): Not a geometric sequence.
# Given an array of integers and a common ratio r, find all triplets of indexes (i, j, k) that follow a
# geometric sequence for i < j < k. It’s possible to encounter duplicate triplets in the array.
# Example:

# Input: nums = [2, 1, 2, 4, 8, 8], r = 2
# Output: 5
# Explanation: Triplet [2, 4, 8] occurs at indexes (0, 3, 4), (0, 3, 5), (2, 3, 4), (2, 3, 5). Triplet
# [1, 2, 4] occurs at indexes (1, 2, 3).
# Time and Space O(N)

def geometric_sequence_triplets(nums: List[int], r: int) -> int:
    # Use 'defaultdict' to ensure the default value of 0 is returned when 
    # accessing a key that doesn’t exist in the hash map. This effectively sets 
    # the default frequency of all elements to 0.
    left_map = defaultdict(int)
    right_map = defaultdict(int)
    count = 0
    # Populate 'right_map' with the frequency of each element in the array.
    for x in nums:
        right_map[x] += 1
    # Search for geometric triplets that have x as the center.
    for x in nums:
        # Decrement the frequency of x in 'right_map' since x is now being
        # processed and is no longer to the right.
        right_map[x] -= 1
        if x % r == 0:
            count += left_map[x // r] * right_map[x * r]
        # Increment the frequency of x in 'left_map' since it'll be a part of the
        # left side of the array once we iterate to the next value of x.
        left_map[x] += 1
    return count