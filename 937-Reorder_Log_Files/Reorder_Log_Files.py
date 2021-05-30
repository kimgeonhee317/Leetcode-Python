
class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        digLogs : list[str] = []
        letLogs : list[str] = []

        for log in logs:
            if log.split()[1].isdigit():
                digLogs.append(log)
            else :
                letLogs.append(log)
        
        letLogs.sort(key=lambda x : (x.split()[1:], x.split()[0]))
        #letLogs.sort(key=letLogs.split()[1:])
        return letLogs+digLogs


logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
print(Solution.reorderLogFiles(Solution, logs))