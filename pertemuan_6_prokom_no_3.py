set_A = {20, 30, 40, 50, 60}
set_B = {25, 30, 35, 40, 45}
set_C= {30, 40, 50, 70, 80}
set_D = {40, 50, 60, 90, 100}
cara_1 = set_A & set_C & set_D
print("Irisan set_A, set_C, dan set_D:", cara_1)
cara_2 = (set_A | set_B) - set_D
print("Gabungan set_A dan set_B, lalu selisihkan dengan set_D:", cara_2)
cara_3 = set_B - set_C
print("Selisih simetris dari set_B dan set_C:", cara_3)
cara_4 = set_A |set_B
cara_5 = set_C|set_D
print("hasil gabungan set_A dan set_B, lalu gabungan dengan set_C dan set_D:", cara_4 & cara_5)
