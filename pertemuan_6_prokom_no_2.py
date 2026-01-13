nilai = set({3,6,9,2,5,7}) 
print("nilai awal :", nilai)

nilai.update([1,4,8,10])
print("setelah di update :", nilai)

for i in [1,3,4,5,7,8,10]:
    nilai.discard(i)
print("setelah di discard:", nilai)

