

def atm(withdrawal,totalamount):
    if withdrawal<=(totalamount-0.50) and withdrawal%5==0 :
        return format(totalamount-(withdrawal+0.50),'.2f')
    else:
        return format(totalamount,'.2f')

    
withdrawal,totalamount = input().split()
withdrawal,totalamount =[int(withdrawal),float(totalamount)]
print(atm(withdrawal,totalamount))
        
                       
                   
