#game tebak nilai kartu
import random

while True:
    bilacak=random.randint(1, 11)
    #print(bilacak)
    #bilb=random.randint(10, 20)
    tebak=input('ketik nilai: kecil/besar:')
    if bilacak <=9:
        hasil='kecil'
    else:
        hasil='besar'
    if tebak ==hasil:
        print('kamu menang')
    else:
        print('kamu kalah')    
    
    #bermain 2orang
    #saya dan komputer
    #saya:menebak
    #komp:kartu
    
    #input(mengacak kartu(11 kartu))
    #input(saya menebak: y: ketik nilai: kecil/besar:)
    


