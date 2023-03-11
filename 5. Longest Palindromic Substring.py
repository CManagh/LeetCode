class Solution(object):
    def longestPalindrome(self, input_string):
        """
        :type s: str
        :rtype: str
        """
        char_count = {}
        max_length = 0
        longest_palindrome = ""

        # If the input string is a single character, return it as the longest palindrome
        if len(input_string) == 1:
            return input_string

        # Count the occurrences of each character in the input string
        for char in input_string:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1

        # Filter the dictionary to keep only characters with multiple occurrences
        char_count = {char: count for char, count in char_count.items() if count > 1}

        # Check all possible palindromes using the filtered characters
        for char in char_count.keys():
            indexes = [i for i, c in enumerate(input_string) if c == char]
            length, palindrome = find_longest_palindrome(input_string, indexes)
            if length > max_length:
                max_length = length
                longest_palindrome = palindrome

        # If no palindromes were found, return the first character as the longest palindrome
        if longest_palindrome == "":
            return input_string[0]
        return longest_palindrome


def find_longest_palindrome(input_string, indexes):
    max_length = 0
    longest_palindrome = ""
    for firstIndex in indexes:
        for secondIndex in indexes:
            if firstIndex == secondIndex:
                pass
            else:
                forward = input_string[firstIndex:secondIndex+1]
                backward = forward[::-1]
                if forward == backward:
                    if len(forward) > max_length:
                        max_length = len(forward)
                        longest_palindrome = forward
    return max_length, longest_palindrome


input = "sadabad"
obj = Solution()
returnVal = obj.longestPalindrome(input)
print(returnVal)
