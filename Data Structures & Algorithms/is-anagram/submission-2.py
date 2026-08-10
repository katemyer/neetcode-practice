class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if length of s == length of t, continue
            #if s slice left to right == t slice right to left
            #return true
        #else return false

        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)