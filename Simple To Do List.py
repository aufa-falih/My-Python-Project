# membuat to do list
# to_do_list = [[nomor urut,aktivitas],[nomor urut,aktivitas]]

# judul
judul = 'TO DO LIST SEDERHANA'

print('='*20)
print(judul)
print('='*20)
print('')


nama = input('Masukkan nama Anda\t: ').capitalize()

list_aktivitas = []
aktivitas = input('\nMasukkan aktivitas\t: ')
list_aktivitas.append(aktivitas)

while True:
    ada_lagi = input('Ada lagi?(y/n): ')
    
    if ada_lagi == 'y':
        aktivitas = input('Masukkan aktivitas\t: ')
        list_aktivitas.append(aktivitas)
        
    elif ada_lagi == 'n':
        break
    else:
        print('Error, ulang')
        continue

print(f'\nHai {nama}, ini To Do List Kamu:')
print('-'*30)
for index,aktivitas in enumerate(list_aktivitas):
        print(f'''{index+1}. {aktivitas}''')
