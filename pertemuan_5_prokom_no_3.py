hasil = int(input("masukan jumlah nilai: "))
total = 0

for i in range (hasil):
    nilai = float(input(f"masukan nilai ke {i+1}: "))
    total += nilai

rata_rata = total // hasil
print(f"rata_rata dari {hasil} nilai adalah: {rata_rata}")