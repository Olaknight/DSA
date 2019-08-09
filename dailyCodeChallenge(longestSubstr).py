class Solution:
    def longestSubstring(self, s):
        temp = []
        longest = 0
        tlen = 0

        x = len(s)

        for i in range(x):
            if s[i] not in temp:
                temp.append(s[i])
                tlen += 1 
            else:
                if tlen > longest:
                    longest = tlen
                    temp = [s[i]]

                tlen = 1

        return longest 

print(Solution().longestSubstring("abrkaabcdefghijjxxx"))