class Solution:
    def countOdds(self, low: int, high: int) -> int:
        l = high - low + 1
        if(l % 2 == 0):
            c = int(l/2)
        elif(l % 2 != 0):
            if(low % 2 == 0):
                c = int(l/2)
            if(low % 2 != 0):
                c = int(l/2)+1
        return c
