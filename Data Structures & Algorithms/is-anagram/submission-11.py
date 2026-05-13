class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        words1 = list(s)
        words2 = list(t)
        sort1 = sorted(words1)
        sort2 = sorted(words2)
        if sort1 == sort2:
            return True
        else:
            return False