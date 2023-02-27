nama_aing = "Mukidi"

nama_aing = input('Input Nama : ')
usia = 24

usia = str(usia) #Konversi

punya_pacar = True

print(nama_aing, "saat ini berusia " + usia)
print("tahun jika dikalikan maka menjadi ", int(usia)*int(usia))

usia = float(usia)
if usia >= 23 : 
    if punya_pacar == False : 
        print('udah tua euy, cepat nikah!')
    else: 
        print('halalin atuh!')
elif usia >= 15 : 
    if punya_pacar == False : 
        print('mantap, fokus aja untuk mengembangkan diri')
    else: 
        print('Masih minta jajan sok-sok an pacaran')
else :
    print('Belajar lagi dek')

#Comment
#print('Ganteng sekali anda!')
"""
    Ini Comment Juga
    Tapi untuk multiple line
"""