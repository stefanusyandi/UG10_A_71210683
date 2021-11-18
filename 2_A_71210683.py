print("############################")
print("Kalkulator Advance Sederhana")
print("############################")
print("1. Menghitung sisa hasil bagi")
print("2. Mmebulatkan ke bawah hasil pembagian")
print("3. Mencari akar kubik sebuah bilangan")

Y = int(input("masukkan menu yang anda pilih: "))
if Y == 1:
    a = int(input("Masukkan bilangan yang ingin dibagi: "))
    b = int(input("Masukkan bilangn pembagi: "))
    c = int(a%b)
    print("Sisa hasil bagi",float(a)," dibagi dengan",float(b),"adalah",float(c))
elif Y==2:
    a = int(input("Masukkan bilangan yang ingin dibagi: "))
    b = int(input("Masukkan bilangn pembagi: "))
    c = int(round(a/b,1))
    print("Hasil pembagian",float(a),"dibagi dengan",float(b),"dibulatkan kebawah adalah",float(c))
elif Y==3:
    a = int(input("Masukkan bilangan yang ingin dicari akar kubiknya "))
    b = int(a**(1/3))
    print("Akar kubik dari",float(a),"adalah",float(b))
else:
    print("Menu yang anda pilih tidak tersedia")

