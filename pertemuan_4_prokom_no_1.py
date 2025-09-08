umur = int(input("masukan umur ="))
nilai = int(input("masukan niali test = "))
lulus = "selamat anda berhak mendapat SIM"
gagal = "Maaf, anda tidak berhak mendapat SIM\nSilahkan coba lagi bulan atau tahun depan"
if (umur > 17):
    if(nilai < 60):
        print()
        print(gagal)
    else:
        print()
        print(lulus)
else: 
    print()
    print(gagal)
    