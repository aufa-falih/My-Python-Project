# Membuat simple game menebak posisi Mowli


# teknis berjalannya game ini
# sambutan dari mowli, ajakan untuk bermain
# user diberikan 4 kotak dan menebak di kotak mana mowli berada

# rules
# user diberikan 3 kali kesempatan
# user menebak dari angka 1 - 3
# jika kesempatan sudah habis, game selesai, mowli bertanya kpd user apakah ingin main lagi atau tidak

# kebutuhan
import random
empty_box = '[ ]'
main_box = [empty_box] * 3
mowli_position = random.randint(1,5)
attempts = 3


# head
title = 'DI MANAKAH MOWLI BERADA???'
print('='*26)
print(title)
print('='*26+'\n')

# input nama user
username = input('Masukkan nama kamu: ').title()

# sambutan
print(f'''
Halo {username}! Kenalin aku Mowli :D, aku mau ngajak kamu main tebak-tebakan mau gaaakk?''')
while True:
    user_decision = input('Mau(y) | Tidak(n): ')

    if user_decision == 'n':
        print('Yahh... Okedeh lain kali aja :()')
        exit
    elif user_decision == 'y':
        print('\nYEAYYY OKE SIMAK BAIK-BAIK YA!!!')
        break
    else:
        print('IHH jawab yang bener >:()')

# mulai game
# soal
print(f'''
HIHIHIHI sekarang aku udah sembunyi di salah satu kotak iniii

{empty_box} {empty_box} {empty_box} {empty_box} {empty_box}

Tugasmu adalah menebak di kotak mana aku bersembunyi :D''')

# tebakan user

# operasi tebakan
while attempts > 0:
    user_answer = int(input('Aku ada di mana hayo [1/2/3/4/5]: '))
    
    if user_answer == mowli_position:
        print(f'WOAHH KAMU BENER, AKU ADA DI KOTAK NOMER {mowli_position} [ >:P ]')
        break
    elif user_answer != mowli_position:
        print(f'HEHEHEH Bukan di situ :P')
        attempts -= 1

# habis
print(f'Yahhh... sayang banget tapi kesempatan kamu udah abis {username}, aku sebenernya ada di kotak nomer {mowli_position} :P')
