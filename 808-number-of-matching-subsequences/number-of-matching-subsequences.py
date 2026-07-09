class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        c=0
        for word in words:
            cu=-1
            for w in word:
                f=1
                cu=s.find(w,cu+1)
                if cu==-1:
                    f=0
                    break
            if f==1:
                c+=1
        return c
            