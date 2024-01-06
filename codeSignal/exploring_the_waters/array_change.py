"""
You are given an array of integers. On each move you are allowed to increase exactly one of
 its element by one. Find the minimal number of moves required to obtain a strictly
 increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
solution(inputArray) = 3.
"""


def solution(input_array: list[int]) -> int:
    increment_count = 0

    for i in range(1, len(input_array)):
        if input_array[i] < input_array[i - 1]:
            increment_count += (input_array[i - 1] - input_array[i]) + 1
            input_array[i] = input_array[i - 1]

    return increment_count


print(solution(input_array=[3, 1, 2]))
