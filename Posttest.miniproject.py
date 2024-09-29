#login nama dan nim
print("SELAMAT DATANG DI PROGRAM KALKULATOR GAJI")
print("============Silahkan Login===============")
nama = input("\nMasukkan nama anda: ") #Memasukkan nama

while True: #looping NIM
    nim = (input("Masukkan NIM anda: ")) #Memasukkan NIM
    if nim.isdigit(): #Memeriksan bahwa NIM terdiri dari digit(integer)
        break #keluar dari loop jika nim berupa integer
    else:
        print("NIM harus terdiri dari angka. Silahkan coba lagi") #Mengulang kembali ke input NIM

while True: #looping PIN
    pin = (input("Masukkan PIN (harus 7 angka): ")) #Memasukkan PIN
    if len(pin) == 7 and nim.isdigit(): #Memeriksa PIN apakah terdiri dari 7 angka dan berupa integer
        print("\n===========Login Berhasil!")
        print(f"Selamat datang, {nama} dengan NIM {nim}.")
        break #keluar dari loop jika sudah memenuhi dua kondisi
    else:
        print("PIN harus terdiri dari 7 angka. Silahkan coba lagi") #Mengulang kembali ke input PIN

#Input jam kerja dan tarif kerja karyawan
while True:
    try:
        jam = float(input("\nMasukkan jumlah jam kerja anda: "))
        tarif = float(input("Masukkan tarif gaji per jam (dalam rupiah): "))
        total = jam*tarif

#Menghitung apakah mendapat bonus
        if jam > 160:
            bonus = (0.1*total) + total
            print("\nSelamat anda mendapatkan bonus gaji  \nTotal gaji : Rp", bonus)
        else:
            print("\nMaaf anda tidak mendapatkan bonus gaji. \nTotal gaji anda : ", total)
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        continue
    
#Menanyakan user apakah ingin menghitung ulang gaji
    while True: #looping di dalam looping
        Tanya = input("\nApakah anda ingin menghitung gaji lagi?\n1. Ya\n2. Tidak\nMasukkan angka: ")
        if Tanya == '1' :
            print("Baik silahkan hitung ulang\n")
            break
        elif Tanya == '2':
            print("============Program Selesai=============")
            exit() #keluar dari semua looping
        else:
            print("Pilihan tidak tersedia, silahkan pilih angka sesuai opsi")