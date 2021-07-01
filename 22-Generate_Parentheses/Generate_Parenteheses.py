class Solution:
    def generateParentheses(self, n: int) -> list[str]:
        sliceGroup : list[str] = []
        Solution.addParentheses(sliceGroup,"", n ,n)
        
        target : list[str] = []
        for slice in sliceGroup:
            if Solution.isParentheses(slice) == True:
                target.append(slice)
        return target

    # step 1 : make all parenthesis case using Recursion
    def addParentheses(sliceGroup, str: str, left, right):
        if (left == 0 and right == 0):
            sliceGroup.append(str)
            return True
        elif (left == 0):
            Solution.addParentheses(sliceGroup, str+')', left, right-1)
        elif (right == 0): 
            Solution.addParentheses(sliceGroup, str+'(', left-1, right)
        else :
            Solution.addParentheses(sliceGroup, str+')', left, right-1)
            Solution.addParentheses(sliceGroup, str+'(', left-1, right)
        
    # step 2 : filtering out the non-Parentheses case   
    def isParentheses(str: str) -> bool:
        flag = 0
        for slice in str:
            if slice == '(':
                flag +=1 
            else :
                flag -=1
                if (flag < 0): return False
        return True

number : int = 3
print(Solution.generateParentheses(Solution, number))
