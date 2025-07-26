



# Given a string of lowercase English letters, rearrange the characters to form a new string
# representing the next immediate sequence in lexicographical (alphabetical) order. If the given
# string is already last in lexicographical order among all possible arrangements, return the
# arrangement that’s first in lexicographical order.
# Example 1:
# Input: s = "abcd"
# Output: "abdc"
# Explanation: "abdc" is the next sequence in lexicographical order after rearranging "abcd".

# Example 2:
# Input: s = "dcba"
# Output: "abcd"
# Explanation: Since "dcba" is the last sequence in lexicographical order, we return the first
# sequence: "abcd".
# Constraints:
# ● The string contains at least one character.
# O(n)

def next_lexicographical_sequence(s: str) -> str:
    letters = list(s)
    # Locate the pivot, which is the first character from the right that breaks 
    # non-increasing order. Start searching from the second-to-last position.
    pivot = len(letters) - 2
    while pivot >= 0 and letters[pivot] >= letters[pivot + 1]:
        pivot -= 1
    # If pivot is not found, the string is already in its largest permutation. In
    # this case, reverse the string to obtain the smallest permutation.
    if pivot == -1:
        return ''.join(reversed(letters))
    # Find the rightmost successor to the pivot.
    rightmost_successor = len(letters) - 1
    while letters[rightmost_successor] <= letters[pivot]:
        rightmost_successor -= 1
    # Swap the rightmost successor with the pivot to increase the lexicographical
    # order of the suffix.
    letters[pivot], letters[rightmost_successor] = (letters[rightmost_successor], letters[pivot])
    # Reverse the suffix after the pivot to minimize its permutation.
    letters[pivot + 1:] = reversed(letters[pivot + 1:])
    return ''.join(letters)