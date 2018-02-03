def cnote(n,y,k,x):
    var=0
    for i in range(n):
        p,c =map(int,input().split())
        if p>=x-y and c<=k:
            var = var+1
            
    if var>0:
        return "LuckyChef"
    else: return "UnluckyChef"
    
                

testcase= int(input())
for i in range(testcase):
    x,y,k,n = map(int,input().split())
    #x,y,k,n = [int(x) for x in input().split()]
    print (cnote(n,y,k,x))    
    







