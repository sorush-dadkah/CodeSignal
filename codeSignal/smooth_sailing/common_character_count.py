"""
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""


def solution(s1: str, s2: str) -> int:
    return sum(min(s1.count(char), s2.count(char)) for char in set(s1))


print(solution("aabcc", "acbaa"))
