# Data Mahasiswa Sederhana

import os
# membersihkan terminal
os.system('cls' if os.name == 'nt' else 'clear')
print('=== Program Data Mahasiswa Sederhana ===\n')

# kebutuhan
angka = 1
data_mahasiswa = {}


# mengambil input data
while True:
    key = str(angka)
    nama = input('Masukkan nama Anda\t\t\t: ').title()
    nim = input('Masukkan NIM Anda\t\t\t: ').upper()
    fakultas = input('Masukkan nama fakultas Anda(singkatan)\t: ').upper()
    program_studi = input('Masukkan program studi Anda\t\t: ').title()
    
    # memasukkan input ke template dictionary mahasiswa
    mahasiswa_template = {
        'nama':nama,
        'nim':nim,
        'fakul':fakultas,
        'prodi':program_studi,
    }
    
    # menambah data dictionary
    data_mahasiswa.update({key:mahasiswa_template}) 
    
    # input yang lain
    ada_lagi = input('\nAda lagi?(y/n)\t\t\t\t: ')
    angka += 1
    
    if ada_lagi == 'n':
        break


# print hasil input data
nomor_data = "No"
nama_mahasiswa = "Nama Mahasiswa"
nim_mahasiswa = "NIM"
fakultas_mahasiswa = "Fakultas"
prodi_mahasiswa = "Program Studi"

head = '=== Data Mahasiswa ==='
print(f'\n{head:^65}')
print('_'*65)
print(f'\n{nomor_data:<5} {nama_mahasiswa:<20} {nim_mahasiswa:<8} {fakultas_mahasiswa:<10} {prodi_mahasiswa:<20}')
print('_'*65)

for index,data in data_mahasiswa.items():
    nomor = index
    NAMA = data_mahasiswa[nomor]['nama']
    NIM = data_mahasiswa[nomor]['nim']
    FAKULTAS = data_mahasiswa[nomor]['fakul']
    PRODI = data_mahasiswa[nomor]['prodi']
    print(f'{nomor:<5} {NAMA:<20} {NIM:<8} {FAKULTAS:<10} {PRODI:<20}')


