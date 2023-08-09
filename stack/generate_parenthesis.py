from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Initialize the output list
        out = []

        # Define a recursive helper function to generate the combinations
        def generate_helper(s: str, left: int, right: int):
            # If we have used all the parentheses, add the combination to the output list
            if left == n and right == n:
                out.append(s)
                return

            # If we have used fewer left parentheses than n, add a left parenthesis and recurse
            if left < n:
                generate_helper(s + "(", left + 1, right)

            # If we have used fewer right parentheses than left parentheses, add a right parenthesis and recurse
            if right < left:
                generate_helper(s + ")", left, right + 1)

        # Call the helper function to generate the combinations
        generate_helper("", 0, 0)

        # Return the output list
        return out


if __name__ == "__main__":
    print(Solution().generateParenthesis(3))
