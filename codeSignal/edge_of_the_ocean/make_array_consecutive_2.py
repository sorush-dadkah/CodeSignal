"""
Ratiorg got statues of different sizes as a present from CodeMaster for his birthday,
each statue having a non-negative integer size. Since he likes to make things perfect,
he wants to arrange them from smallest to largest so that each statue will be bigger
than the previous one exactly by 1. He may need some additional statues to be able to
 accomplish that. Help him figure out the minimum number of additional statues needed.

Example

For statues = [6, 2, 3, 8], the output should be
solution(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.
"""

# 2, 3, 6, 8


def solution(statues: list[int]) -> int:
    statues = sorted(statues)
    statues_needed = 0

    for i in range(1, len(statues)):
        diff = statues[i] - statues[i - 1] - 1
        if diff > 0:
            statues_needed += diff

    return statues_needed


print(solution(statues=[6, 2, 3, 8]))
