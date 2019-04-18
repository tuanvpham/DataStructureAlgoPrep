class Solution:
    def reverse(self, x: int) -> int:
        strNum =  str(x)
        isNegative = False
        finalString = ""
        for c in reversed(strNum):
            if c == '-':
                isNegative = True
            else:
                finalString += c
        if isNegative:
            finalString = '-' + finalString
        if(abs(int(finalString)) < ((1 << 31) - 1)):
            return int(finalString)
        return 0
            
