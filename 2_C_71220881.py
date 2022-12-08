numbers = input("Masukkan angka:")
hitung  = input("Masukkan angka yang dihitung :")


sum = 0
for each in numbers:
    if each == hitung:
        sum = sum + 1

print ("numbers",hitung,"muncul sebanyak",sum,"kali")
