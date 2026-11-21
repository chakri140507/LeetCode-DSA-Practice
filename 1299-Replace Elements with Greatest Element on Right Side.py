class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        i = len(arr)-1
        m = -1
        while i>=0:
            temp = arr[i]
            arr[i] = m
            if temp>m:
                m = temp
            i-=1
        return arr

        
