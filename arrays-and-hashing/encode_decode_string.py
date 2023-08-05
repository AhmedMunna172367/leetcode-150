# alternate src: https://leetcode.ca/2016-08-27-271-Encode-and-Decode-Strings/


class Codec:
    def encode(self, strs):
        # Encode a list of strings into a single string
        encoded = ""
        for s in strs:
            # Add the length of the string and a delimiter to the encoded string
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s):
        # Decode a string into a list of strings
        decoded = []
        i = 0
        while i < len(s):
            # Find the position of the next delimiter
            delimiter = s.index("#", i)
            # Extract the length of the next string
            length = int(s[i:delimiter])
            # Extract the next string and add it to the list of decoded strings
            decoded.append(s[delimiter + 1 : delimiter + 1 + length])
            # Update the index to point to the next position after the extracted string
            i = delimiter + 1 + length
        return decoded


def test_codec():
    codec = Codec()

    # Test empty input
    assert codec.decode(codec.encode([])) == []

    # Test single string input
    assert codec.decode(codec.encode(["hello"])) == ["hello"]

    # Test multiple string input
    input_strs = ["hello", "world", "foo", "bar"]
    assert codec.decode(codec.encode(input_strs)) == input_strs

    # Test input with special characters
    input_strs = ["hello#", "world#", "#foo", "bar"]
    assert codec.decode(codec.encode(input_strs)) == input_strs

    # Test input with empty strings
    input_strs = ["hello", "", "world", ""]
    assert codec.decode(codec.encode(input_strs)) == input_strs


if __name__ == "__main__":
    test_codec()
