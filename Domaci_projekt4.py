##for i in range (4):
##    print ('a')
##    
##for cislo_radku in range (5):
##    print ('Řádek', cislo_radku)
##    
##for druha_mocnina in range (5):
##    vysledek = int (druha_mocnina * druha_mocnina)
##    print (druha_mocnina, 'na', 'druhou', 'je', vysledek)
##
##for pocet_opakovani in range (5):
##    for pismeno_x in range (5):
##        print ('X', end='')
##    print ()
##
##
##for pocet_radku in range (5):
##    for nasobitel in range (5):
##        print (pocet_radku * nasobitel, end='')
##    print ()
##        
##
##for pocet_opakovani in range (4):
##    for pismeno_x in range (pocet_opakovani + 1):
##        print ('X', end='')
##    print ()
##
##
##for cislo_radku in range (4):
##    if cislo_radku == 0:
##        print ('první řádek')
##    else:
##        print ('není první')

##for cislo_radku in range (5):
##    print ('X', end='')
##    for pismeno_x in range (4):
##        if cislo_radku == 0:
##            print (' X', end='')
##        elif cislo_radku == 4:
##            print (' X', end='')
##        else:
##            print ('  ', end='')
##    print (' X', end='')
##    print ()


##for cislo_radku in range (5):
##    for cislo_sloupce in range (6):
##        if cislo_radku * cislo_sloupce == 0:
##            print ('X', '', end = '')
##        elif cislo_radku * cislo_sloupce == 30:
##            print ('X', '', end = '')
##    print ()

   
#X X X X X X
#X         X
#X         X
#X         X
#X X X X X X
##
##cislo1 = int (input ('Zadej první číslo:'))
##cislo2 = int (input ('Zadej druhé číslo:'))
##cislo3 = int (input ('Zadej třetí číslo:'))
##soucet = cislo1 + cislo2 + cislo3
##if soucet > 10:
##    print ('Součet čísel je větší než 10.')
##else:
##    print ('Součet čísel není větší než 10.')
##                  
##cislo = int (input ('Zadej celé číslo:'))
##if cislo%2==0:
##    print ('Číslo', cislo, 'je sudé.')
##else:
##    print ('Číslo', cislo, 'je liché.')

##for i in range (101):
##    if i%3==0 and i%5==0:
##        print ('bum-bác')
##    elif i%5==0:
##        print ('bác')
##    elif i%3==0:
##        print ('bum')
##    else:
##        print (i)


soucet = 0
for i in range(5):
 cisloi = int (input ('Zadej $i číslo:'))
 soucet = soucet + cisloi
 if soucet > 10:
    print ('Součet čísel je větší než 10.')
 else:
    print ('Součet čísel není větší než 10.')
                  
