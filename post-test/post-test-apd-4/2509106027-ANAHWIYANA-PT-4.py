username = "Anah"
password = "027"

max_attempts = 5
attempts = 0
authenticated = False

while attempts < max_attempts and not authenticated:
    input_username = input("Masukan Usernama  :")
    input_password = input("Masukan Possword :")

    if input_username == username and input_password == password:
         print("Login berhasil!")
         authenticated = True
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if remaining_attempts == 0:
             print("Batas Percobaan Telah Sampai Kebatas Maksimum !")
        else:
            print(f"Username atau password salah. Sisa percobaan: {remaining_attempts}")

if authenticated:
    while True:
        print("Menu:")
        print("1.Lanjut Menggunakan Program")
        print("2. Keluar")

        pilihan = input("Pilih menu (1/2): ")
        break

if pilihan == '1' :
    print("Selamat Melanjutkan Ke Tahap Selanjutnya")
else :
    print("Program berhenti")

print("==================================================")
print("==========Pengecekan Syarat Rental Mobil==========")
print("==================================================")
                    
usia = int(input("~ Masukan Usia Anda                     : "))
memiliki_sim_A = input("~ Apakah Anda memiliki SIM? (ya/tidak)  : ")
deposit = int(input("~ Masukan Jumlah Deposit Anda           : "))
pengalaman_mengemudi = int(input("~ Berapa Tahun Pengalama Mengemudi Anda :"))
memiliki_sim_A = memiliki_sim_A . strip() . lower() == 'ya'

if usia < 21 :
    print("Tolak : Usia Tidak Mencukupi")
elif not memiliki_sim_A:
    print("Tolak : Tidak Memiliki SIM A")
elif deposit < 500000 :
    print("Tolak : Deposit Tidak Mencukupi")
elif pengalaman_mengemudi < 4 :
    print("Setuju Untuk Mobil Standar Saja")
else :
    print("Setuju Untuk Semua Jenis Mobil")

print("===================================================")
print("========Terima Kasih Selamat Datang Kembali========")
print("===================================================")