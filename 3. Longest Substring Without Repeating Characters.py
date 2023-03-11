class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        finalCount = 0
        count = 0
        store = []

        for index, letter in enumerate(s):
            print(store)
            print(count)
            # todo keep in bounds
            # if count=len(s):
            #     break
            # if not starting letter
            # print(store)
            if len(store) > 0:
                # check if letter different
                if letter not in store:
                    store.append(letter)
                    count += 1
                # letter same
                else:
                    ##remove first occurence of duplicate unless letter = letter-1
                    if len(store) > 0:
                        if store[-1] == letter:
                            store = []
                            if index < len(s):
                                finalCount = max(count, finalCount)
                                count = 0
                    else:
                        store.remove(letter)
                        store.append(letter)
            else:
                store.append(letter)
                count += 1
        return max(count, finalCount)


obj = Solution()
te = "aab"
out = obj.lengthOfLongestSubstring(te)
print(out)
