def find_largest(a, b, c):
    return max(a, b, c)

#Tentukan fungsinya
angka_pertama = float(input("Enter first number: "))
angka_kedua= float(input("Enter second number: "))
angka_ketiga= float(input("Enter third number: "))

# Find and print the largest number
largest = find_largest(angka_pertama, angka_kedua, angka_ketiga)
##Inisialisasi daftar kosong untuk menyimpan angka
print(f"The largest number is: {largest}")
## Bandingkan setiap angka dengan angka terbesar
##Menampilkan hasil
