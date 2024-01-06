"""
Two arrays are called similar if one can be obtained from another by swapping at
 most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
solution(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
solution(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
solution(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.
"""


def solution(a_list: list[int], b_list: list[int]) -> bool:
    return (sorted(a_list) == sorted(b_list)
            and sum([a != b for a, b in zip(a_list, b_list)]) <= 2)


al = [1, 2, 3]
bl = [2, 1, 3]
print(solution(al, bl))
