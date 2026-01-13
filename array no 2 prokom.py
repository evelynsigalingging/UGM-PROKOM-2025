data_nama = []
for i in range(5):
    nama = input(f"masukkan nama ke-{i+1}: ")
    data_nama.append(nama)

print("\nDaftar nama teman:")
for i, nama in enumerate(data_nama):
    print(f"Indeks {i}: {nama}")

ganti_indeks = int(input("\nMau mengganti nama pada indeks ke berapa?(0-4): "));

ganti_nama = input("masukan nama baru:")
data_nama[ganti_indeks]= ganti_nama

print("data nama setelah di perbarui")
for i, nama in enumerate(data_nama):
    print(f"indeks{i}: {nama}")


      
