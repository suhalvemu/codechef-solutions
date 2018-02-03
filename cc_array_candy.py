def candy(c,list_n):
    for i in range(len(list_n)):
            c=c-list_n[i]
            if c<0:
                return 'No'
    return 'Yes'    

T=int(input())
for i in range(T):
   n,c=[int(x) for x in input().split()]
   list_n=list(map(int,input().split()))
   print (candy(c,list_n))
