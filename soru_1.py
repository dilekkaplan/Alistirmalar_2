#iki basamaklı mastermind oyunu
#kullanııcya üç giriş hakkı tanım

import random
pc=str(random.randint(9,99))

while pc[0]==pc[-1]:
    pc=str(random.randint(9,99))

while pc[0]!=pc[-1]:
    break



while True:
    user=input("Lütfen 9 ile 99 arasında ve rakamları farklı bir tamsayı giriniz:")
    dogruyer=0
    yanlisyer=0

    while int(user) >98 or int(user) <10 or (user)[0]==(user)[-1]:
        print("HATA!")
        user=input("Lütfen 9 ile 99 arasında ve rakamları farklı bir tamsayı giriniz:")  
        
    if pc == user:
        print("TEBRİKLER! DOĞRU TAHMİN!Bilgisayarın aklında tuttuğu sayı:",pc,"idi")
        break
    
    if  user[1]==pc[1] or user[0]==pc[0]:
        dogruyer+=1        

    elif user[1]==pc[0] and user[0]==pc[1]: 
        yanlisyer=-2

    elif user[1]==pc[0] or user[0]==pc[1]: 
        yanlisyer=-1

    print("Rakamını doğru tahmin ettiğiniz basamak sayısı:",dogruyer,"\nDogru rakamı yanlis yerde tahmin ettiğiniz rakam sayısı:",yanlisyer,"\nTekrar deneyin!")

if user!=pc:
    print("Yanlış tahmin.Bilgisayarın aklında tuttuğu sayı :",pc,"idi.")

  






