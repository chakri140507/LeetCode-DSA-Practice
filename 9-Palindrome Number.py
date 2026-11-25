class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        original = x
        ans = 0
        while(x>0):
            rem = x%10
            ans = ans*10 + rem
            x = x//10
        if ans == original:
            return True
        else:
            return False


        
