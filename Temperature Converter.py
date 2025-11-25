# Pengubah Suhu Sederhana 

# program mulai
print("===== Program Pengubah Suhu Sederhana =====\n")
print("Anda dapat mengubah suhu dari Celsius ke Fahrenheit, Kelvin, atau Reamur.\n")

while True:
    # input suhu dalam celsius
    celsius = float(input("Masukkan suhu dalam Celsius: "))
    suhu_tujuan = input("Ubah ke ( Fahrenheit(f) / Kelvin(k) / Reamur(r) ): ").lower()
    
    # mengubah suhu berdasarkan pilihan user
    if suhu_tujuan == 'f' or suhu_tujuan == 'fahrenheit':
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit}°F")
        break
    elif suhu_tujuan == 'k' or suhu_tujuan == 'kelvin':
        kelvin = celsius + 273.15
        print(f"{celsius}°C = {kelvin}K")
        break
    elif suhu_tujuan == 'r' or suhu_tujuan == 'reamur':
        reamur = celsius * 4/5
        print(f"{celsius}°C = {reamur}°R")
        break
    else:
        print("Error, ulangi")
        continue

# program selesai
print("Terima kasih telah menggunakan program pengubah suhu!")