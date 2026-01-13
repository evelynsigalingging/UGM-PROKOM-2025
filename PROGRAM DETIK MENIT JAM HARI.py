n=int(input("jumlah_detik: "))

a = 60 * 60 * 24

HARI = n // (60 * 60 * 24)
b = a * HARI
c = n % (60 * 60 * 24)

JAM = c // (60*60)
d = JAM * (60*60)
e = c % (60 * 60)

MENIT = e // 60
DETIK = e % 60

print(f"{n}DETIK = {HARI} HARI, {JAM} JAM, {MENIT} MENIT, {DETIK} DETIK")
