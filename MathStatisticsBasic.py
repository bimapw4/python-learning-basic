def angkaUrut(x, end, angka):
    while x < end:
        i = 0
        while i < end:
            if angka[x] < angka[i]:
                y = angka[x]
                angka[x] = angka[i]
                angka[i] = y
            i = i + 1
        x = x + 1

def deviasiAngka(ragam):
    x = 0
    y = 0
    input = ragam
    while True:    #This simulates a Do Loop
        y = y + 1
        x = y * y
        if not(x < input): break   #Exit loop
    i = input - x
    if i < -0:
        y = y - 1
        x = y * y
        i = input - x
        z = 0
        loop = 0
        max = 0
        while loop < 9:
            z = z + 0.1
            hasil = (2 * y + z) * z
            if hasil < i:
                if max < hasil:
                    max = hasil
                else:
                    loop = 10
            else:
                z = z - 0.1
                loop = 10
            loop = loop + 1
        y = y + z
    print("standar deviasi= " + str(y))

def inputAngka(end, x, angka):
    while x < end:
        print("input angka ke " + str(x + 1))
        angka[x] = float(input())
        x = x + 1

def meanAngka(x, end, angka):
    mean = [0] * (2)
    
    mean[0] = 0
    while x < end:
        mean[0] = mean[0] + angka[x]
        x = x + 1
    mean[1] = mean[0] / end
    valueMean = mean[1]
    
    return valueMean

def medianAngka(angka):
    median = (angka[4] + angka[5]) / 2
    print("median = " + str(median))

def minMaxAngka(angka):
    print("angka terbesar = " + str(angka[9]))
    print("angka terkecil= " + str(angka[0]))

def modusAngka(x, end, angka):
    modus = [0] * (4)
    
    modus[2] = 0
    while x < end:
        i = 0
        modus[3] = 0
        while i < end:
            if angka[x] == angka[i]:
                modus[1] = angka[x]
                modus[3] = modus[3] + 1
                if modus[2] < modus[3]:
                    modus[0] = modus[1]
                    modus[2] = modus[3]
            i = i + 1
        x = x + 1
    if modus[2] > 1:
        print("modus = " + str(modus[0]))
    else:
        print("modus = tidak ada ")

def rangeAngka(angka):
    range = angka[9] - angka[0]
    print("Range = " + str(range))

def simpanganAngka(x, end, angka, mean):
    simpangan = [0] * (10)
    
    simpanganRata = 0
    while x < end:
        mutlak = angka[x] - mean
        if mutlak < -0:
            simpangan[x] = mutlak * -1
        else:
            simpangan[x] = mutlak
        simpanganRata = simpanganRata + simpangan[x]
        x = x + 1
    simpanganRata = simpanganRata / end
    print("simpangan rata rata = " + str(simpanganRata))

def varianAngka(x, end, angka):
    varian = [0] * (4)
    
    varian[0] = 0
    varian[1] = 0
    while x < end:
        varian[0] = varian[0] + angka[x]
        varian[1] = varian[1] + angka[x] ** 2
        x = x + 1
    varian[2] = varian[0] ** 2
    varian[3] = (end * varian[1] - varian[2]) / (end * (end - 1))
    valueVarian = varian[3]
    
    return valueVarian

# Main
angka = [0] * (10)

end = 10
x = 0
inputAngka(end, x, angka)

angkaUrut(x, end, angka)

modusAngka(x, end, angka)

rataRata = meanAngka(x, end, angka)
print("mean = " + str(rataRata))

minMaxAngka(angka)

medianAngka(angka)

rangeAngka(angka)

simpanganAngka(x, end, angka, rataRata)

ragam = varianAngka(x, end, angka)
print("varian = " + str(ragam))

deviasiAngka(ragam)