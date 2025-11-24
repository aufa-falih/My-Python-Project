# Data Mahasiswa Sederhana

# kebutuhan
angka = 0
data_mahasiswa = {}


# mengambil input data
while True:
    key = 'a' + str(angka)
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


# ngeprint hasil data
for index,data in data_mahasiswa.items():
    nomor = index
    NAMA = data_mahasiswa[nomor]['nama']
    NIM = data_mahasiswa[nomor]['nim']
    FAKULTAS = data_mahasiswa[nomor]['fakul']
    PRODI = data_mahasiswa[nomor]['prodi']
    print(f'{nomor:<5} {NAMA:<20} {NIM:<8} {FAKULTAS:<10} {PRODI:<20}')

