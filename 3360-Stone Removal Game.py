class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove = 10
        t = 0
        while n>=remove:
            n -= remove
            remove-=1
            t +=1
        if t%2 != 0:
            return True
        else:
            return False

        
