while True:
    print('Program Kalkulator Diskon Toko Buku Pustaka Cerdas')
    
    try:
        jumlah_buku = int(input('Masukkan Jumlah Buku Yang Dibeli: '))
        harga_buku = int(input('Masukkan Harga per Buku (Rp): '))

        if jumlah_buku >= 1 and jumlah_buku <= 5:
            print(f'Total harga yang dibayarkan: Rp{harga_buku}')
        elif jumlah_buku >= 6 and jumlah_buku <= 9:
            sebelum_diskon = jumlah_buku * harga_buku
            print(f'Total Harga Sebelum Diskon Rp{sebelum_diskon}')
            diskon_1 = (jumlah_buku * harga_buku) * 0.05
            diskon_1 = sebelum_diskon - diskon_1
            print('Diskon: 5%')
            print(f'Total Harga Yang Dibayarkan: Rp{diskon_1}')
        elif jumlah_buku >=10:
            sebelum_diskon = jumlah_buku * harga_buku
            print(f"Total Harga Sebelum Diskon: Rp{sebelum_diskon}")
            diskon_2 = (jumlah_buku * harga_buku) * 0.10
            diskon_2 = sebelum_diskon - diskon_2
            print('Diskon: 10%')
            print(f'Total Harga Yang Dibayarkan: Rp{diskon_2}')
        else:
            print('Inputan salah, coba kembali input angka yang benar')
            continue
        
        break
    except ValueError:
        print('Inputan salah, coba kembali input angka yang benar')