"""
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
solution(inputString) = true;
For inputString = "abac", the output should be
solution(inputString) = false;
For inputString = "a", the output should be
solution(inputString) = true.
"""


def solution(input_string: str) -> bool:
    return input_string == input_string[::-1]


print(solution("aabaa"))
