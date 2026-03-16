class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
       
            chars = list(word)

        
            n = len(chars)
            for i in range(n):
                for j in range(0, n-i-1):
                    if chars[j] > chars[j+1]:
                        chars[j], chars[j+1] = chars[j+1], chars[j]

        
            key = ""
            for c in chars:
                key += c

            if key in d:
                d[key].append(word)
            else:
                d[key] = [word]

        result = []
        for k in d:
            result.append(d[k])

        return result

            