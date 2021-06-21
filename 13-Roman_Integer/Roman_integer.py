class Solution:
    def romanToInt(self, s: str):
        roman = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        conNumber = 0
        for index in range(0, len(s)): 
            if(index == len(s)-1): # last word
                conNumber += roman[s[index]]   
                break
            if(roman[s[index]]<roman[s[index+1]]):
                conNumber -= roman[s[index]]
            else : conNumber += roman[s[index]]

        return conNumber
        
print(Solution.romanToInt(Solution, "MCMXCIV"))