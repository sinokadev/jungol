n = int(input())

def abmodm(a,b):
    return ((a%1000000007)*(b%1000000007))%1000000007

result = n

for i in range(n-1):
    result = abmodm(result, n)

print(result)