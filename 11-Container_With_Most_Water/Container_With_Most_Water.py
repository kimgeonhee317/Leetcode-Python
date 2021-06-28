class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = 0
        left = 0
        right = 1

        while right < len(height) :
            if(height[left] < height[right]):
                right+=1
                continue
            else :
                temp_area = Solution.getArea(height[left], height[right], right-left)
                if(temp_area >= area) : # find big one
                area = temp_area
            
     

        return area
    
    def getArea(left: int, right: int, width: int) -> int:
        return min(left, right)*width


print(Solution.maxArea(Solution, [1,8,6,2,5,4,8,3,7]))       