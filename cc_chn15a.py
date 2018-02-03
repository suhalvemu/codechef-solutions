def mutation(array_n,k):
    count=0
    for i in range(len(array_n)):
        if (array_n[i]+k)%7==0:
            count =count+1
    return count

testcase=int(input())
for i in range(testcase):
    n,k=[int(x) for x in input().split()]
    array_n=list(map(int,input().split()))
    print(mutation(array_n,k))

