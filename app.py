username = "1"
password = "1"

database_buku = [
    ["Judul 1", "Penulis 1", "Tahun 1"],
    ["Judul 2", "Penulis 2", "Tahun 2"],
    ["Judul 3", "Penulis 3", "Tahun 3"]
]

def login():
    while True:
        login_user = input("Masukkan username: ")
        login_pass = input("Masukkan password: ")
        if login_user == username and login_pass == password:
            print("Login berhasil")
            return True
        else:
            print("Login gagal")

def lihat_buku():
    print("Daftar buku perpustakaan:")
    for i, buku in enumerate(database_buku, 1):
        print(f"%d. Judul: %s, Penulis: %s, Tahun: %s" %(i, buku[0], buku[1], buku[2]))
    balik_menu = input("silahkan tekan enter untuk kembali ke menu awal")
    if balik_menu == "":
        menu()

def tambah_buku():
    judul_buku = input("Masukkan judul buku yang ingin ditambahkan: ")
    penulis_buku = input("Masukkan penulis buku yang ingin ditambahkan: ")
    tahun_buku = input("Masukkan tahun buku yang ingin ditambahkan: ")
    database_buku.append([judul_buku, penulis_buku, tahun_buku])
    print("Buku berhasil ditambahkan.")
    menu()

def hapus_buku():
    print("Hapus buku")

def peminjaman_buku():
    print("Peminjaman buku")

def menu():
    print("")
    print("")
    print("===Menu Perpustakaan===")
    print('1. Lihat daftar buku')
    print('2. Tambah buku baru')
    print('3. Hapus buku dari daftar')
    print('4. Peminjaman buku')
    pilihan_menu = input('Silahkan pilih menu (masukkan nomor): ')
    if pilihan_menu == '1':
        lihat_buku()
    elif pilihan_menu == '2':
        tambah_buku()
    elif pilihan_menu == '3':
        hapus_buku()
    elif pilihan_menu == '4':
        peminjaman_buku()

login()
menu()
