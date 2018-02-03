from collections import Counter
from itertools import permutations

def islovely(lovely):
    count=0
    perms=[''.join(p) for p in permutations('chef')]
    for i in range(len(lovely)-3):
        if lovely[i:i+4] in perms:
            count = count + 1
            
    if count>0:
        return 'lovely'+' '+str(count)
    else:
        return 'normal'

testcase=int(input())
list1=[]
for i in range(testcase):
    string=input()
    res=islovely(string)
    list1.append(res)

for i in range(len(list1)):
    print(list1[i])




    
