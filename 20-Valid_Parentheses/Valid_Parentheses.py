class Solution:
    def isValid(self, s):
        openShape = ['(','{','[']
        # closeShape = [')','}',']']
        flag = 0
        for char in s:
            if char in openShape:
               flag+=1
            else : flag-=1
        if flag == 0 :
            return True
        else : return False

print(Solution.isValid(Solution, "(){"))