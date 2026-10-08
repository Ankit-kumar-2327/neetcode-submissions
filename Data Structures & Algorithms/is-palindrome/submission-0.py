class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while(left < right):
            if(not self.isValid(s[left])):
                left += 1
            elif(not self.isValid(s[right])):
                right -= 1
            else:
                if(s[left].lower() != s[right].lower()):
                    return False
                else:
                    left += 1
                    right -= 1
        
        return True
    
    def isValid(self, ch):
        ch = ord(ch)
        if ((ch >= 65 and ch <= 90) or (ch >= 97 and ch <= 122) or (ch >= 48 and ch <= 57)):
            return True
        
        return False
        