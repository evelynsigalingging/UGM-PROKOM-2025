buah_buahan = {
    "Apel": 15000,
    "Jeruk": 10000,
    "Anggur": 25000
}

print("Harga Jeruk:", f"Rp{buah_buahan['Jeruk']:,}")

buah_buahan["Mangga"] = 12000
print("\nDictionary setelah menambahkan Mangga",buah_buahan)

buah_buahan["Anggur"] = 20000
print("\ndictionary setelah memperharui harga anggur:", buah_buahan)

del buah_buahan["Jeruk"]
print("\ndictionary buah_buahan terbaru:", buah_buahan)