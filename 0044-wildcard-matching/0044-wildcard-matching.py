class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def match(ss,ps):
            if len(ss)!=len(ps):
                return False
            for sv,pv in zip(ss,ps):
                if sv!=pv and pv!='?':
                    return False
            return True
        s="@"+s+"%"
        p="@"+p+"%"
        i=0
        for ps in p.split('*'):
            while not match(s[i:i+len(ps)],ps):
                i+=1
                if i>=len(s):
                    return False
            i+=len(ps)
        return True

        