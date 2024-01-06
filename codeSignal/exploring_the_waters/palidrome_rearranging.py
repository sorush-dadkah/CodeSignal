"""
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
"""


def solution(input_string: str) -> bool:
    counter = {char: input_string.count(char) for char in input_string}
    return sum(item % 2 != 0 for item in counter.values()) <= 1


# counter = {a: 2, b: 2, c: 1, x: 1}
s = "aabb"
# s = "aabbc"
# s = "aabbcx"
print(solution(input_string=s))
