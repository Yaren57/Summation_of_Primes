son_sayi = 2000000
toplam = 0
for sayi in range(2, son_sayi + 1):
    i = 2
    for i in range(2, sayi):
        if (int(sayi % i) == 0):
            i = sayi
            break
            
    if i is not sayi:
        toplam = toplam + sayi
print(toplam)
