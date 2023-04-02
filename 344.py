from typing import List

class Solution:
    
    def reverseString(self, s: List[str], i=0, j=-1)-> None:
        """
        Do not return anything, modify s in-place instead.
        """
           

        if i == len(s) // 2:    
            return s
        
        s[i], s[j] = s[j], s[i]
        
        j -= 1
        i += 1
        
        
        return self.reverseString(s, i, j)
        