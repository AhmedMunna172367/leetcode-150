import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to store the anagrams
        anagram_dict = collections.defaultdict(list)

        # Iterate through each word and group it with its anagrams
        for word in strs:
            # Sort the letters in the word to create a key for the anagram dictionary
            key = "".join(sorted(word))
            anagram_dict[key].append(word)

        # Return the values of the anagram dictionary as a list of lists
        return list(anagram_dict.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
