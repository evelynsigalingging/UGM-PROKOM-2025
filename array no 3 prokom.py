from array import array
angka=array('i', [2, 7, 8, 10, 12])
print("isi array:", angka)
print("jumlah elemen dalam array:",len(angka))

#menghitung elemen
total = 0
for num in angka:
    total += num
print("jumlah total elemen", total)

#menghitung rata rata
rata_rata= total/len(angka)
print("rata rata nilai array adalah", rata_rata)
