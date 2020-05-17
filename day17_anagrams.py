class Solution:
    def findAnagrams(self, s: str, p: str):
        from collections import Counter
        dic1 = Counter(p)
        dic2 = Counter(s[:len(p)-1])
        out = []
        for i in range(len(p)-1, len(s)):
            dic2[s[i]] += 1          #new character updation in dic2
            index = i-len(p) + 1     # storing index of the character
            firstch = s[index]         # First holds the char in the window
            if dic1 == dic2:        # If two dictionaries are the same, we find an anagram
                out.append(index)
            if dic2[firstch] == 1:      
                del dic2[firstch]       
            else:
                dic2[firstch] -= 1      #count-1 from dic
        return out
