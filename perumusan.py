print("menghitung rumus segitiga dan persegi")
x = input("masukan bidang datar=")

if x == "segitiga":
    a = float(input(" masukan alas: "))
    b = float(input("masukan tinggi: "))
    print("luas segitiga:", 0.5*a*b)
elif x == "persegi":
    a = int(input(" masukan sisi persegi"))
    print(" luas nilai persegi:", a*a)

else:
    print(" masukin bidang datar dong")

    
