class Solution:
    def longestCommonPrefix(self, strArray):
        commonPrefix = strArray[0]
        for str in strArray:
            #print (commonPrefix, str)
            commonPrefix = self.getCrossArea(self, commonPrefix, str)
        return commonPrefix

    def getCrossArea(self, str1, str2):
        crossArea = ""
        for slice in range(min(len(str1),len(str2))):
            if str1[slice] == str2[slice]:
                crossArea+=str1[slice]
            else: break
        return crossArea
        
strArray = ["flower","flow","flight"]
print(Solution.longestCommonPrefix(Solution, strArray))
#Solution.getCrossArea("aabsdgasdasd", "aabewgege")


