import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        # Define a dictionary to map opening and closing parentheses
        p_map = {"(": ")", "[": "]", "{": "}"}

        # Use a stack to keep track of opening parentheses
        stack = []

        # Iterate over each character in the string
        for ss in s:
            # If the character is an opening parenthesis, push it onto the stack
            if ss in p_map.keys():
                stack.append(ss)
            # If the stack is empty and we encounter a closing parenthesis, the string is invalid
            elif len(stack) == 0:
                return False
            # If the character is a closing parenthesis, pop the last opening parenthesis from the stack
            # and check if it matches the closing parenthesis
            else:
                last = stack.pop()
                if ss != p_map[last]:
                    return False

        # If the stack is empty, the string is valid
        return len(stack) == 0


class TestSolution(unittest.TestCase):
    def test_valid_string(self):
        s = Solution()
        self.assertTrue(s.isValid("()"))
        self.assertTrue(s.isValid("()[]{}"))
        self.assertTrue(s.isValid("{[]}"))
        self.assertTrue(s.isValid("({[]})"))

    def test_invalid_string(self):
        s = Solution()
        self.assertFalse(s.isValid("("))
        self.assertFalse(s.isValid(")"))
        self.assertFalse(s.isValid("(]"))
        self.assertFalse(s.isValid("([)]"))
        self.assertFalse(s.isValid("{{}"))
        self.assertFalse(s.isValid("}"))
        self.assertFalse(s.isValid("]"))
        self.assertFalse(s.isValid(")()"))
        self.assertFalse(s.isValid("([)]"))
        self.assertFalse(s.isValid("({[}])"))

    def test_empty_string(self):
        s = Solution()
        self.assertTrue(s.isValid(""))

    def test_single_char_string(self):
        s = Solution()
        self.assertFalse(s.isValid("("))
        self.assertFalse(s.isValid(")"))
        self.assertFalse(s.isValid("["))
        self.assertFalse(s.isValid("]"))
        self.assertFalse(s.isValid("{"))
        self.assertFalse(s.isValid("}"))
        self.assertFalse(s.isValid("a"))


if __name__ == "__main__":
    unittest.main()
