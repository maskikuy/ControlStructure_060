def evaluasi_kinerja(percentage):
    ## input dan mengembalikan evaluasi kinerja yang sesuai.
    if percentage >= 90:
        return "Excellent performance"
    ## Meminta untuk memasukkan persentase siswa.
    elif percentage >= 80:
        return "Very Good performance"
    elif percentage >= 70:
        return "Good performance"
    elif percentage >= 60:
        return "Average performance"
    else:
        return "perbaiki kembali"

# masukan untuk memastikan bahwa masukan tersebut berupa angka antara 0 dan 100.
percent = float(input("Enter the percentage: "))
## output untuk masukan presentasi
result = evaluate_performance(percent)
print(result)
## cetak hasilnya
