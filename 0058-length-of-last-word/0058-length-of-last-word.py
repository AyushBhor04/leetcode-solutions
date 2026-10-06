class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        splitted_words=s.split()
        return len(splitted_words[-1])