class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_val  = 0

        lr = 0
        s1 = set()
        for rr in range(len(s)):

            while s[rr] in s1:
                s1.remove(s[lr])
                lr+=1

            s1.add(s[rr])
            max_val = max(max_val,rr-lr+1)

        return max_val