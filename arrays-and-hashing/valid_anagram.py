class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the strings have the same length
        if len(s) != len(t):
            return False

        # Count the frequency of each letter in both strings
        s_count = [0] * 26
        t_count = [0] * 26
        for i in range(len(s)):
            s_count[ord(s[i]) - ord("a")] += 1
            t_count[ord(t[i]) - ord("a")] += 1

        # Check if the frequency of each letter is the same in both strings
        for i in range(26):
            if s_count[i] != t_count[i]:
                return False

        return True


if __name__ == "__main__":
    # Test the isAnagram method with an example
    assert Solution().isAnagram(s="munna", t="annum") is True
