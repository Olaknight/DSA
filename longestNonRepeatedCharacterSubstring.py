class Solution:
    def longestSubstring(self, s):
        start = 0
        seen = {}
        max_len = 0

        for end in range(len(s)):
            if s[end] in seen.keys():
                start = max(start, seen[s[end]] + 1)
            seen[s[end]] = end
            max_len = max(max_len, end - start + 1)

        return max_len
            
print(Solution().longestSubstring("abrkaabcdefghijjxxx"))