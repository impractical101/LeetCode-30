class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        def check(magazine, ransomNote):
            if (len(ransomNote)==0):
                return True
        emit = ransomNote.pop()
        if emit in magazine:
            magazine.pop(emit)
            check(magazine,ransomNote)
        else:
            return False 
        
        return check(ransomNote, magazine)

        
        
            
            
"""               
return not len(Counter(ransomNote) - Counter(magazine))"""
        

  
"""
magazine.pop(word)
                x = ransomNote.index(word)
                y = magazine.index(word)
                magazine[y] = ''
                while(a != list(ransomNote)):
                    a.append(word)
                    word = ransomNote[x+1]
                return 1
            else:
                return 0   """
"""
x = ransomNote.index(word)
            if (word in magazine):
                word = ransomNote[x+1]
                return 1
            else:
                return 0
"""
             

