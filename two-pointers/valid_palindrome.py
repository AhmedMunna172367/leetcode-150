import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = self.clean(s)

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left, right = left + 1, right - 1

        return True

    def clean(self, s):
        # Remove all non-alphanumeric characters from the string
        return "".join(c for c in s if c.isalnum())


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        self.assertTrue(self.solution.isPalindrome(""))

    def test_single_character_string(self):
        self.assertTrue(self.solution.isPalindrome("a"))

    def test_palindrome_string(self):
        self.assertTrue(self.solution.isPalindrome("racecar"))

    def test_non_palindrome_string(self):
        self.assertFalse(self.solution.isPalindrome("hello"))

    def test_palindrome_string_with_spaces(self):
        self.assertTrue(self.solution.isPalindrome("A man a plan a canal Panama"))

    def test_non_palindrome_string_with_spaces(self):
        self.assertFalse(self.solution.isPalindrome("not a palindrome"))

    def test_palindrome_string_with_punctuation(self):
        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal: Panama"))

    def test_non_palindrome_string_with_punctuation(self):
        self.assertFalse(self.solution.isPalindrome("not, a palindrome!"))


if __name__ == "__main__":
    unittest.main()
