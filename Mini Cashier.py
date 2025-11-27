# latihan menggunakan fungsi

import os
os.system('cls' if os.name == 'nt' else 'clear')

# mini cashier (kasir mini)
title = "WARUNG MALIH"
print("="*30)
print(f'{title:^30}')
print("="*30)
print('')

# teknis program:
# input list harga barang -> ditotal semuanya -> diskon untuk kondisi tertentu misal: membership -> pajak misal: PPN 12% -> total akhir belanjaan

# kebutuhan:

# nama user
username = input('Masukkan nama Anda \t\t\t: ').title()
print('-'*50)

# input list harga customer
list_harga = []
while True:
    input_harga = int(input("Masukkan harga belanjaan Anda \t\t: "))
    list_harga.append(input_harga)
    ada_lagi = input("Ada lagi? (y/n)\t\t\t\t: ").lower()
    if ada_lagi == "n":
        break


# fungsi total harga awal
def total_awal(belanjaan):
    belanjaan_copy = belanjaan.copy()
    hasil_total_awal = sum(belanjaan_copy)
    return hasil_total_awal

hasil_belanjaan = total_awal(list_harga)

# fungsi pajak PPN 12%
def pajak_ppn(setelah_diskon):
    pajak = 11
    hasil_pajak = setelah_diskon + (setelah_diskon*pajak//100)
    return hasil_pajak

total_setelah_pajak = pajak_ppn(hasil_belanjaan)


# fungsi diskon untuk kondisi tertentu
diskon_member = 20
user_member = input("Langganan membership? (y/n)\t\t: ").lower()
if user_member == "y":
    hasil_diskon = total_setelah_pajak - (total_setelah_pajak*diskon_member//100)

# total akhir belanjaan
elif user_member == "n":
    total_akhir = total_setelah_pajak
else:
    print("Error")

# print akhir
print('-'*50)
print(f'Total Harga Awal \t\t\tRp {hasil_belanjaan}')
print(f'Pajak PPN 11% \t\t\t\tRp {total_setelah_pajak}')
if user_member == "y":
    print(f'Diskon Membership \t\t\tRp {hasil_diskon}')
    print(f'Total Akhir \t\t\t\tRp {hasil_diskon}')
else:
    print(f'Total Akhir \t\t\t\tRp {total_akhir}')

# pembayaran
print('-'*50)
pembayaran = int(input('Masukkan nominal pembayaran \t\t: '))
if user_member == "y":
    kembalian = pembayaran - hasil_diskon
else:
    kembalian = pembayaran - total_akhir
print(f'Kembalian \t\t\t\tRp {kembalian}')

# penutup
print('='*50)
print(f'''Terimakasih {username} telah berbelanja di WARUNG MALIH
            Silakan datang kembali :D''')

# akhir program