"1'den n'e kadar olan sayıların çarpımını rekürsif fonks. yardımı ile yazdırır."

def carpim(n):
    if n==1:
        return 1
    else:
        return n*carpim(n-1)
