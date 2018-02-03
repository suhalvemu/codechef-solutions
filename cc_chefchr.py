from collections import Counter





def islovely(lovely):
    counter=Counter(lovely)
    print(counter['c'],counter['h'],counter['e'],counter['f'])

testcase=int(input())

for i in range(testcase):
    string=input()
    islovely(string)






    
