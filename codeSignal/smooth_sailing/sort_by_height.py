"""
Some people are standing in a row in a park. There are trees between them which cannot be moved.
Your task is to rearrange the people by their heights in a non-descending order
without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
"""


def solution(peoples_height: list[int]) -> list[int]:
    heights_sorted = sorted(x for x in peoples_height if x != -1)
    heights_sorted_index = 0

    for index, height in enumerate(peoples_height):
        if height > 0:
            peoples_height[index] = heights_sorted[heights_sorted_index]
            heights_sorted_index += 1

    return peoples_height


print(solution(peoples_height=[-1, 150, 190, 170, 160, -1]))