"""
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
solution(inputArray) = ["aba", "vcd", "aba"].
"""


def solution(input_array) -> list[str]:
    max_length = max(len(string) for string in input_array)
    return [string for string in input_array if len(string) == max_length]


print(solution(["aba", "aa", "ad", "vcd", "aba"]))
