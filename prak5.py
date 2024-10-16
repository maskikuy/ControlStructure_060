# Command 1: Tentukan fungsi untuk menghasilkan pola
def generate_pattern(n):
    pattern = []
    for i in range(1, n + 1):
        row = ' '.join(str(i) * i)
        pattern.append(row)
    return pattern

try:
    # Command 2: Dapatkan masukan dari pengguna
    n = int(input("Enter the number of rows for the pattern: "))

    # Command 3: input validasi
    if n <= 0:
        raise ValueError("Number of rows must be a positive integer")

    # Command 4: Hasilkan pola
    result = generate_pattern(n)

    # Command 5: cetak hasil
    print("Here's your pattern:")
    for row in result:
        print(row)

except ValueError as e:
    print(f"Invalid input: {e}")