class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s)-1
        while lp < rp :
            print(s[lp].upper() , s[rp].upper())
            print(lp, rp)
            print(s[lp].upper() != s[rp].upper())
            
            if  s[lp].isalnum() == False or s[lp] == " ":
                lp += 1
                continue
                

            if s[rp].isalnum() == False or s[rp] == " ":
                rp -= 1
                continue

            print(s[lp].upper() , s[rp].upper())
            print(lp, rp)
            print(s[lp].upper() != s[rp].upper())

            if s[lp].upper() != s[rp].upper() :
                return False
      
            lp += 1
            rp -= 1 

        return True
