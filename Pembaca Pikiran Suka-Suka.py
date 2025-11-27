# membaca pikiran user
import random
import os
os.system('cls' if os.name == 'nt' else 'clear')

# head
print("="*30)
print('''
Hai, Selamat datang di program Pembaca Pikiran :D
Kamu percaya gak kalo aku bisa baca pikiranmu?''')

believe_it_or_not = input("\n(y/n): ").lower()

if believe_it_or_not == "n":
    print("Oke bye.")
    exit

print('''
Oke bagus :D, sebelum kita mulai, kenalin aku Pepi
Kalo kamu namanya siapa?
''')

username = input("Masukkan nama Kamu: ").title()

print(f'''
Oke {username}, Sekarang pikirkan angka dari 1-100''')

pikiran_user = input("Kamu milih angka berapa: ")

print(f'''
HAHA! Aku tau Kamu pasti milih angka {pikiran_user} kan?
jago banget ya aku >:D

Sekarang gantian, aku akan milih angka dari 1-100
dan tugasmu menebak aku lagi mikir angka berapa''')

pikiran_pepi = random.randint(1,100)
while True:
    user_answer = int(input("Tebakanmu: "))

    if user_answer == pikiran_pepi:
        print(f"Wow... Keren banget {username} ternyata kamu lebih jago :O")
        break
    elif user_answer != pikiran_pepi:
        print(f"Yah... Salah, aku mikir angka {pikiran_pepi} :P")
        break
    else:
        print(f"TEBAK YANG BENER!!!")

print(f'''
HEHE Makasih ya {username} udah main game suka-suka aku :3''')