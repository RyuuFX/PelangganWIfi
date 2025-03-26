tarif = {
    'R': [2000, 4500, 6500],
    'C': [5000, 7000, 10000],
    'V': [7500, 10000, 15000]
}

def hotspot():
    while True:
        print("<===========================>")
        print("|       Kode Pelanggan      |")
        print("<===========================>")
        print("R - (Reguler)")
        print("C - (Special)")
        print("V - (VIP)")
        print("Q - (Keluar)")
        kode = input("Masukkan kode pelanggan : ").upper()
        if kode == 'Q':
            print("Kembali ke menu utama...\n")
            break
        if kode not in tarif:
            print("Kode tidak valid, coba lagi.\n")
            continue

        try:
            pemakaian = int(input("Masukkan jumlah pemakaian MB: "))
            biaya = tarif[kode][0] if pemakaian <= 50 else tarif[kode][1] if pemakaian <= 80 else tarif[kode][2]
            print(f"Biaya penggunaan: {biaya}\n")
        except ValueError:
            print("Masukkan angka yang valid.\n")
