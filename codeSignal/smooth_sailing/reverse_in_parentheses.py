"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
solution(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
solution(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
solution(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
"""


def solution(input_string: str) -> str:
    stack = []

    for char in input_string:
        if char == ")":
            temp = ""
            while stack[-1] != "(":
                temp += stack.pop()
            stack.pop()

            for c in temp:
                stack.append(c)
        else:
            stack.append(char)

    return "".join(stack)


print(solution("foo(bar)baz"))
