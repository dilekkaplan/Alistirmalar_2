#Shellde superasal(n) girildiğinde n sayısı super asal ise true, değilse false döndürür.
#Bu program ise beş basamaklı superasalları dondurur.


def superasal(n):
    asal_mi= True
    
    if n>9:
        for i in range(2,n):

            if  n%i==0:
                asal_mi=False
                break

            else:
                asal_mi=True

        if asal_mi==True:
            return(superasal(int(str(n)[:-1]))) 
                       

    elif n<=9:
        if n in [2,3,5,7]:
            asal_mi=True

        else:
            asal_mi=False                   
                
                    
    if asal_mi==True:
        return True
    else:
        return False


for a in range(1000,10000):
    if superasal(a)==True:
        print(a,end=" ")


            

