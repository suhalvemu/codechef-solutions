n,k = [ int(x) for x in input().split()]
count=0
for i in range(n):
    n=int(input())
    if n%k==0:
        count +=1


print (count)        
