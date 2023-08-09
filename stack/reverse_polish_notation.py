import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: list[int] = []
        for t in tokens:
            # If the token is a number, push it onto the stack
            if t not in ["+", "-", "*", "/"]:
                if t[0] == "-" and len(t) > 1:
                    # If the number is negative, convert it to an integer and push it onto the stack
                    stack.append(-int(t[1:]))
                else:
                    # If the number is positive, convert it to an integer and push it onto the stack
                    stack.append(int(t))
            else:
                # If the token is an operator, pop the top two elements from the stack and apply the operator
                second, first = stack.pop(), stack.pop()
                if t == "+":
                    val = first + second
                elif t == "-":
                    val = first - second
                elif t == "*":
                    val = first * second
                else:
                    # If the operands have opposite signs, use math.trunc() to truncate towards zero
                    if first * second < 0:
                        val = math.trunc(first / second)
                    else:
                        # Otherwise, use integer division to compute the result
                        val = first // second
                # Push the result back onto the stack
                stack.append(val)

        # The final result is the only element left on the stack
        return stack[-1]


if __name__ == "__main__":
    # Example usage
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(Solution().evalRPN(tokens=tokens))
