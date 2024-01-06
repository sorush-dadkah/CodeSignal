"""
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

solution(picture) = ["*****",
                     "*abc*",
                     "*ded*",
                     "*****"]
"""


def solution(picture: list[str]) -> list[str]:
    bordered_picture = ["*" * (len(picture[0]) + 2)]

    for row in picture:
        bordered_picture.append(f"*{row}*")

    bordered_picture.append("*" * (len(picture[0]) + 2))

    return bordered_picture


print(solution(picture=["abc", "ded"]))
