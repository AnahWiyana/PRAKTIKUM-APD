# mata kuliah
# matakuliah = ["APD","Kalkulus","Orsikom"]

# matakulilah = [ ]

# print(dir(list))

# membaca list
# print(matakuliah[0:2])

# print(matakuliah[-1])

# print(matakuliah[1:3:2]

# matakuliah.append("Matdis")

# print(matakuliah1)

# matakuliah.insert(2,"Matematika")
# matakuliah.insert(0,"Matematika")
# print(matakuliah)

# praktikum["mahasiswa",]

# print(praktikum[4][0])

# matakuliah = ['PTI','APD','Kalkulus','Diskrit']

# for index, i in enumerate (matakuliah) :
#     print(f"mata kuliah ke {index} : {i}")

# matakuliah.remove("Kalkulus")
# matakuliah.pop()

# hapus = matakuliah.pop(3)

# print(hapus)

# list = [1,2,3]

# nilai = [4,5,6]

# hasil = list+nilai

# print (sum(list)/len(list))

# kelas = (
#     ["Ridho", "Lian", "Nabil"],
#     ["Daffa", "Dante", "Santoso"],
#     ["Pernanda", "Riyadi", "Ahnaf"],
# )

# kelas[1].insert(1,"Bakil")
# print(kelas[1])

# for i in kelas :
#     for nama in i:
#         print(nama)







laundry_sepatu = []  # List untuk menyimpan semua data laundry

def tampilkan_data():
    print("\n=== DATA LAUNDRY SEPATU ===")
    if not laundry_sepatu:
        print("Belum ada data laundry.")
    else:
        print("{:<4} {:<15} {:<15} {:<15} {:<10} {:<12}".format(
            "No", "Nama", "Jenis Sepatu", "Layanan", "Harga", "Status"
        ))
        print("-" * 75)
        for i, data in enumerate(laundry_sepatu):
            print("{:<4} {:<15} {:<15} {:<15} Rp{:<8} {:<12}".format(
                i + 1, data["nama"], data["jenis_sepatu"], data["layanan"], data["harga"], data["status"]
            ))

def tambah_data():
    print("\n=== TAMBAH DATA LAUNDRY ===")
    nama = input("Masukkan nama pelanggan: ")
    jenis_sepatu = input("Masukkan jenis sepatu (Sneakers/Boots/Sandal): ")
    layanan = input("Masukkan jenis layanan (Cuci Biasa/Deep Clean/Repaint): ")

    # Tentukan harga otomatis berdasarkan layanan
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
    laundry_sepatu.append({
        "nama": nama,
        "jenis_sepatu": jenis_sepatu,
        "layanan": layanan,
        "harga": harga,
        "status": status
    })
    print("✅ Data berhasil ditambahkan!")

def ubah_data():
    tampilkan_data()
    print("\n=== UBAH DATA LAUNDRY ===")
    index = int(input("Masukkan nomor data yang ingin diubah: ")) - 1
    if 0 <= index < len(laundry_sepatu):
        data = laundry_sepatu[index]
        print(f"Mengubah data untuk {data['nama']}")
        data["status"] = input("Masukkan status baru (Proses/Selesai/Diambil): ")
        print("✅ Status berhasil diperbarui!")
    else:
        print("❌ Nomor tidak valid!")

def hapus_data():
    tampilkan_data()
    print("\n=== HAPUS DATA LAUNDRY ===")
    index = int(input("Masukkan nomor data yang ingin dihapus: ")) - 1
    if 0 <= index < len(laundry_sepatu):
        deleted = laundry_sepatu.pop(index)
        print(f"🗑️ Data untuk {deleted['nama']} berhasil dihapus!")
    else:
        print("❌ Nomor tidak valid!")

# Menu utama
while True:
    print("\n=== MENU UTAMA ===")
    print("1. Tambah Data Laundry")
    print("2. Lihat Semua Data")
    print("3. Ubah Status Laundry")
    print("4. Hapus Data Laundry")
    print("5. Keluar")

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
        print("👋 Terima kasih! Program Laundry Sepatu selesai.")
        break
    else:
        print("❌ Pilihan tidak valid!")