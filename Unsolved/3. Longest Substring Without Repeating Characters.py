class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # setup storing variables
        store = []
        reverseStore = []
        maxLength = 0
        length = 0
        # loop through String
        for char in s:
            # initilise first value in each list
            if length == 0:
                store.append(char)
                reverseStore.append(char)
                length = 1
                maxLength = 1
            else:
                # if the character is in the normal list store, then get the length and start a new list with the new
                # starting character
                if char in store:
                    length = len(store)
                    if length > maxLength:
                        maxLength = length
                    store = [char]
                # if character isn't in the list, append to existing list and increment count
                else:
                    store.append(char)
                    length = len(store)
                    if length > maxLength:
                        maxLength = length
                # check if the character is in the reverse list
                if char in reverseStore:
                    # check if the last character of the list in the same as the checking character, if so start new
                    # list. used for this case: pwwkew -> wke
                    if reverseStore[-1] == char:
                        reverseStore = [char]
                    else:
                        # check if the first character in the list is the same as the checking character, if so,
                        # remove first value and append latest character. used for this case: abcabd -> cabd
                        if reverseStore[0] == char:
                            reverseStore.remove(char)
                            reverseStore.append(char)
                        # last condition to consider - ohvhjdml-need to remove first occurence of h, and all values
                        # before it from list -> vhjdml
                        else:
                            index = reverseStore.index(char)
                            reverseStore = reverseStore[index+1:]
                            reverseStore.append(char)
                    length = len(reverseStore)
                    if length > maxLength:
                        maxLength = length
                else:
                    reverseStore.append(char)
                    length = len(reverseStore)
                    if length > maxLength:
                        maxLength = length

        return maxLength



obj = Solution()
te1 = "ohvhjdml"
te2 = " "
out = obj.lengthOfLongestSubstring(te1)
# out2 = obj.sol2(te2)
print(out)
# print(out2)
