V = input("Masukkan artikel yang ingin dipindai: ")
X = input("Masukkan nama klub favorit anda: ")
Z = input("Masukkan skor yang ingin dicari: ")
if X in V and Z in V:
    print("Hasil pencarian ditemukan")
elif X in V:
    print("Hanya",X,"yang ditemukan pada artikel ini")
elif Z in V:
    print("Hanya skor",Z,"yang ditemukan pada artikel ini")
else:
    print("Hasil pencarian",X,"dan",Z,"tidak ditemukan")