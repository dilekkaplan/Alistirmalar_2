#Shellde superasal(n) girildiğinde n sayısı super asal ise true, değilse false döndürür.
#Bu program çalıştırıldığında dört basamaklı süper asal sayıları döndürür.(Beş basamaklı yavaş çalıştı çünkü:O


def superasal(n):
    asal_mi= True

    for i in range(1,len(str(n))):
            if len(str(n))!=1:
                for bolen in range(2,int(n)):
                    if n==1:
                        asal_mi=False
                        break

                    if  n%bolen==0:
                        asal_mi=False
                        break

                    else:
                        bolen+=1
                        asal_mi=True

                if asal_mi==True:
                    n=int(str(n)[1:])


            if len(str(n))==1:
                if n==1:
                        asal_mi=False
                        break
                
                for bolen in range(2,int(n)):
                    
                        
                    if  int(n)%bolen==0:
                        asal_mi=False
                        break

                    else:
                        bolen+=1
                        asal_mi=True

                if asal_mi==True:
                    return True
                else:
                    return False

                
for i in range(1000,10000):
    if superasal(i)==True:
        print(i,end=" ")
    



    
            

