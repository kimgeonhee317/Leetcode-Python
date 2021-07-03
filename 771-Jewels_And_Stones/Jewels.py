
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelDict = {}

        for jewel in jewels: #setting jewelDict
            jewelDict[jewel] = 0

        for stone in stones:
            if stone in jewels:
                jewelDict[stone] += 1
        
        count = 0
        for key in jewelDict.keys():
            count += jewelDict[key]
        
        return count


jewels = "z"
stones = "ZZ"
print(Solution.numJewelsInStones(Solution,jewels,stones))