while True:
    print("<===================>")
    print("|    Hotspot Modi   |")
    print("<===================>")
    print("1. Biaya Pemakaian")
    print("2. Keluar")
    pilih = int(input("Masukkan Pilihan :"))
        
    if pilih == 1:
        from modi import hotspot
        hotspot()
    elif pilih == 2:
        print("Terimakasih sudah mencoba program ini...")
        break
    else :
        print("Pilihan tidak tersedia,mohon pilih kembali")