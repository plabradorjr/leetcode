class Solution:
    def reverseWords(self, s: str) -> str:
        array = s.split()
        return " ".join(reversed(array))
