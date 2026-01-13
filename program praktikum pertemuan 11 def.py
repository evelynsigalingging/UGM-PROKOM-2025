buku = []
def show_data():
    if len(buku)<= 0:
        print("BELUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s" % (indeks, buku[indeks]))
def insert_data(): #fungsi untuk menambah data
    buku_baru = input("judul buku: ")
    buku.append(buku_baru)
def edit_data(): #fungsi untuk mengedit data
    show_data()
    indeks = int(input("inputkan ID buku: "))
    if indeks < 0 or indeks >= len(buku):
        print("ID salah")
    else:
        buku_baru = input("judul baru: ")
        buku[indeks] = buku_baru
def delete_data(): #fungsi untuk menghapus data
    show_data()
    indeks = int(input("inputkan ID buku: "))
    if indeks < 0 or indeks >= len(buku):
        print("ID salah")
    else:
        buku.pop(indeks)
def show_menu(): #fungsi untuk menampilkan menu
    print("\n")
    print("---------MENU--------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    menu = input("Pilih menu> ")
    print("\n")
    if menu == "1":
        show_data()
    elif menu == "2":
        insert_data()
    elif menu == "3":
        edit_data()
    elif menu == "4":
        delete_data()
    elif menu == "5":
        exit()
    else:
        print("Menu salah")
while True:
    show_menu()