class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            a=list(s)
            b=list(t)
            for i in a:
                for j in b:
                    if i==j:
                        b.remove(j)
                        break
            if len(b)==0:
                return True
            else:
                return False
        else:
            return False


        