class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t) and len(s)==len(t)