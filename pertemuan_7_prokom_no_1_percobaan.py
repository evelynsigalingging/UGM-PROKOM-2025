buah_buahan= {
    "apel" : 15000,
    "jeruk" : 10000,
    "anggur" :25000,
}
print("daftar harga buah:")
for nama in buah_buahan:
    print(f"{nama} : Rp.{buah_buahan[nama]:}")

print("harga jeruk:")
for nama in buah_buahan:
    if nama == "jeruk":
        print(f"{nama}: Rp.{buah_buahan[nama]:}")