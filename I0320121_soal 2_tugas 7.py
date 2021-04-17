# Program Menggunakan Fungsi Numerik
import math

a = int(input("Masukkan jumlah angka yang akan dihitung : "))
data =[]
i = 1
while i <= a:
    b = float(input("Nilai ke-{}: ".format(i)))
    data.append(float(b))
    i = 1 + i
#min dan max
print("\nNilai terendah : ",min(data))
print("Nilai tertinggi : ",max(data))
print()

rerata = float((sum(data))/a)
#ceil
print("Pembulatan rata-rata ke atas : ",math.ceil(rerata))
#floor
print("Pembulatan rata-rata ke bawah : ",math.floor(rerata))

#sqrt
print('\nMenghitung nilai akar suatu bilangan')
x = float(input("Masukkan angka : "))
print("Akar", x, "adalah", math.sqrt(x))
print()