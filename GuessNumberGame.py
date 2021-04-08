import random

ready = input('Apakah anda siap bermain(Y/T) :')

while ready == "y":

  batasAtas = 100
  batasBawah = 0
  tr = 0

  hasil = "false"

  print("Tentukan angka yang akan ditebak 0-100")
  angka = random.randint(40,60)

  while hasil == "false":
    yOrn = input('Apakah angka yang akan ditebak lebih besar dari ' + str(angka) + " (Y/T):")

    if angka == batasBawah:
      tr = 1
    else:
      tr = 0

    if yOrn == "y":
      batasBawah = angka
    elif yOrn == "t":
      batasAtas = angka
    
    if tr == 1:
      hasil = "true"
      print(batasAtas)

    angka = int((batasBawah + batasAtas) / 2)
  ready = input('Ingin bermain lagi? (Y/T) :')
  