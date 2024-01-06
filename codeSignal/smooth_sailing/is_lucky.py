"""
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky
if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example

For n = 1230, the output should be
solution(n) = true;
For n = 239017, the output should be
solution(n) = false.
"""


def solution(n: int) -> bool:
    n_str = str(n)
    length = len(n_str)

    if length % 2 != 0:
        return False

    first_half = sum(int(digit) for digit in n_str[: length // 2])
    second_half = sum(int(digit) for digit in n_str[length // 2:])

    return first_half == second_half


print(solution(n=1230))
