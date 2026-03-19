class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l=""
        for i in s :
            if i.isalnum() :
                l=l+i
        if l==l[::-1]:
            return True
        else:
            return False
                      
        pass
        