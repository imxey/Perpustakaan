username = "1"
password = "1"

database_buku = [
    ["Judul 1", "penulis 1", "Tahun 1"],
    ["Judul 2", "penulis 2", "Tahun 2"],
    ["Judul 3", "penulis 3", "Tahun 3"]

]
def login():
    while True:
        login_user=input("Enter username : ")
        login_pass=input("Enter password : ")
        if login_user==username and login_pass==password:
            print("Login successful")
            return True
        else:
            print("Login failed")
def lihat_buku():
    print("Daftar buku perpustakaan: ")
    for i in range(len(database_buku[0])):
        print("%s. %s" %([i+1], database_buku[i]))

def tambah_buku():
    print("Tambah")
def hapus_buku(): 
    print("Hapus")

def peminjaman_buku():
    print("Peminjaman")
def menu():
    print('1. Lihat buku')
    print('2. Tambah buku')
    print('3. Hapus buku dari daftar buku')
    print('4. Peminjaman buku')
    pilihan_menu = input('Silahkan Pilih Menu (pilih berdasarkan nomor)')
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
