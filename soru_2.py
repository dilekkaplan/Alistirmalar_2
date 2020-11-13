"Bu fonksiyon 1'den n'e kadar olan sayıların toplamını rekürsif fonks yardımı ile yazdırır."

def topla(i):
    if i==1:
        return 1

    else:
        return i+topla(i-1)
    
