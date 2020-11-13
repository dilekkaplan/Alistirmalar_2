#ilk 30 Fibbonaci sayısını rekülsif olarak yazdıran program
def fibo(x):
        
    if x==1:
        return 1

    elif x==2:
        return 1

    else:
        return fibo(x-2)+ fibo(x-1)

for i in range(1,31):
    print(fibo(i), end=" ")
    
    
    
  
    



            
    
    

        



  




        

