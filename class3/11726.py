import sys
n = int(sys.stdin.readline().rstrip())
result = [0,1,2]

for i in range(3,n+1):
    result.append(result[i-1]+result[i-2])
    
print(result[n]%10007)