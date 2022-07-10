def asal_bul(x):
    asal_sayilar = [2,3]
    for i in range(5,x,2):
        for b in range(3,int(i**0.5)+2,2):
            if i % b == 0:
                break
            elif b+2>int(i**0.5):
                asal_sayilar.append(i)
                break
    return asal_sayilar

def asal_toplam(n):
    asal_liste = asal_bul(n)
    asal_toplam = 0
    for i in range(0,len(asal_liste),1):
        asal_toplam += asal_liste[i]
    return asal_toplam

if __name__=="__main__":
    print(asal_toplam(2000000))
