class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        r=""
        for word in words:
            s=0
            for i in word:
                ch=ord(i)-97
                s+=weights[ch]
            ch2=122-(s%26)
            r+=chr(ch2)    
        return r        