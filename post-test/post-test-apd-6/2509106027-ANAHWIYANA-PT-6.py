import os

username = input ( "Username : ")
password = input ( "Password :")

if username == "Laundry sepatu" and password == "247" :
    print ("Login berhasih")
    os.system('cls')
else :
    print ("Login gagal")
    exit()

laundry_sepatu = {}
nomor_urut = 1

def tampilkan_data () :
    print ("===== DATA LAUNDRY SEPATU =====")
    if not laundry_sepatu :
        print (" Belum Ada Data ")
    else :
        print (" NO :  NAMA :  JENIS SEPATU :   LAYANAN :   HARGA :   STATUS :") 
        print("-----------------------------------------------")
        for nomor, data in laundry_sepatu.items():
            print(f"{nomor}. {data['nama']} - {data['jenis_sepatu']} - {data['layanan']} - Rp{data['harga']} - {data['status']}")

def tambah_data():
    global nomor_urut
    print("===== TAMBAH DATA LAUNDRY =====")
    nama = input("Masukkan nama pelanggan: ")
    jenis_sepatu = input("Masukkan jenis sepatu (Sneakers/Boots/Sandal): ")
    layanan = input("Masukkan jenis layanan (Cuci Biasa/Deep Clean/Repaint): ")

    if layanan.lower() == "cuci biasa":
        harga = 30000
    elif layanan.lower() == "deep clean":
        harga = 50000
    elif layanan.lower() == "repaint":
        harga = 70000
    else:
        print("Layanan tidak dikenali, harga diset Rp0.")
        harga = 0

    status = "Proses"
    laundry_sepatu[nomor_urut] = ({
        "nama": nama,
        "jenis_sepatu": jenis_sepatu,
        "layanan": layanan,
        "harga": harga,
        "status": status
    })
    nomor_urut += 1
    print(" Data berhasil ditambahkan!")

def ubah_data():
    tampilkan_data()
    print("===== UBAH STATUS LAUNDRY =====")
    index = int(input("Masukkan nomor data yang ingin diubah: ")) 
    if index in laundry_sepatu:
        data = laundry_sepatu[index]
        print(f"Mengubah status untuk {data['nama']}")
        data["status"] = input("Masukkan status baru (Proses/Selesai/Diambil): ")
        print("Status berhasil diperbarui!")
    else:
        print("Nomor tidak valid!")

def hapus_data():
    tampilkan_data()
    print("===== HAPUS DATA LAUNDRY =====")
    index = int(input("Masukkan nomor data yang ingin dihapus: ")) - 1
    if index in laundry_sepatu:
        deleted = laundry_sepatu.pop(index)
        print(f"Data untuk {deleted['nama']} berhasil dihapus!")
    else:
        print("Nomor tidak valid!")

while True:
    contoh_data = ("Rafi", "Sneakers", "Deep Clean", 50000, "Selesai")
    print("Contoh data :", contoh_data)
    print("------------------------------------------------------------------")
    print("===== MENU UTAMA =====")
    print("1. Tambah Data Laundry")
    print("2. Lihat Semua Data")
    print("3. Ubah Status Laundry")
    print("4. Hapus Data Laundry")
    print("5. Keluar")
    print("-------------------------------------------------------------------")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        ubah_data()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "5":
        print(" Terima kasih! Program Laundry Sepatu selesai.")
        break
    else:
        print(" Pilihan tidak valid!")
   