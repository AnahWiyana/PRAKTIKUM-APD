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