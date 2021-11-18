Z = input("Mendatar/Menurun?: ")
if Z == "Mendatar":
    y = int(input("Masukkan kolom: "))
    print("#"*y)
elif Z == "Menurun":
    y =int(input("Masukkan baris: "))
    print("*\n"*y)
else:
    print("Pola tidak dikenali")        

