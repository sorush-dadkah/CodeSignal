"""
Given an array of integers, find the pair of adjacent elements that has the largest product
and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.

7 and 3 produce the largest product.
"""


def solution(input_array: list[int]) -> float:
    max_product = float("-inf")

    for i in range(1, len(input_array)):
        product = input_array[i] * input_array[i - 1]
        if product > max_product:
            max_product = product

    return max_product


print(solution(input_array=[-3, 6, -2, -5, 7, 3]))
