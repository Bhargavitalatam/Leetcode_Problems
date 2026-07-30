class Solution:
    def minimumPushes(self, word: str) -> int:
        r=0
        for i in range(len(word)):
            r+=i//8+1
        return r
        