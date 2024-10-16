## Definisikan fungsi Fibonacci
def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

# Dapatkan masukan dari pengguna
n = int(input("Enter the number of Fibonacci terms to generate: "))
# Validasi masukan

result = fibonacci(n)
# Hasilkan seri Fibonacci
print(f"Fibonacci series up to {n} terms: {result}")
##Cetak seri Fibonacci
