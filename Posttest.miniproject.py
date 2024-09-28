#login nama dan nim
print("SELAMAT DATANG DI PROGRAM KALKULATOR GAJI")
print("============Silahkan Login===============")
nama = input("\nMasukkan nama anda: ")

while True:
    nim = (input("Masukkan NIM anda: "))
    if nim.isdigit():
        break
    else:
        print("NIM harus terdiri dari angka. Silahkan coba lagi")

while True:
    pin = (input("Masukkan PIN (harus 6 angka): "))
    if len(pin) == 7 and nim.isdigit():
        print("\n===========Login Berhasil!")
        print(f"Selamat datang, {nama} dengan NIM {nim}.")
        break
    else:
            print("PIN harus terdiri dari 7 angka. Silahkan coba lagi")

#Input jam kerja dan tarif kerja karyawan
while True:
    try:
        jam = float(input("\nMasukkan jumlah jam kerja anda: "))
        tarif = float(input("Masukkan tarif gaji per jam (dalam rupiah): "))
        total = jam*tarif
        if jam >= 160:
            bonus = (0.1*total) + total
            print("\nSelamat anda mendapatkan bonus gaji setelah mencapai target kerja 160 jam. \nTotal gaji : Rp", bonus)
        else:
            print("\nMaaf anda tidak mendapatkan bonus gaji karena tidak mencapai target kerja 160 jam. \nTotal gaji anda : ", total)
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        continue
    while True:
        Tanya = input("\nApakah anda ingin menghitung gaji lagi?\n1. Ya\n2. Tidak\nMasukkan angka: ")
        if Tanya == '1' :
            print("Baik silahkan hitung ulang\n")
            break
        elif Tanya == '2':
            print("============Program Selesai=============")
            exit()
        else:
            print("Pilihan tidak tersedia, silahkan pilih angka sesuai opsi")