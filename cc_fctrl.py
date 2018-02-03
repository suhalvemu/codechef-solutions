def factorial(num):
    n,count,r=1,0,0
    while num>0:
        n=n*num
        num=num-1
    while n:
        if n%10==0:
            count +=1
            n=n//10
    return count        
                
testcase=int(input())

result=[]
for _ in range(testcase):
    i = int(input())
    res=factorial(i)
    result.append(res)


for i in range(len(result)):
    print(result[i])
