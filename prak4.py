# Command 1: Tentukan fungsi untuk menghasilkan angka ganjil
def generate_odd_numbers(n):
    return [num for num in range(1, n+1) if num % 2 != 0]

try:
    # Command 2: masukkan dari user
    n = int(input("Enter the upper limit for odd numbers: "))

    # Command 3: input validasi
    if n <= 0:
        raise ValueError("Upper limit must be a positive integer")

    # Command 4: Hasilkan angka ganjil
    result = generate_odd_numbers(n)

    # Command 5: hasilkan angka ganjil
    print(f"Odd numbers up to {n}: {result}")

    # Command 6: hitung dan hasilkan
    count = len(result)
    sum_of_odds = sum(result)
    average = sum_of_odds / count if count > 0 else 0

    print(f"Count of odd numbers: {count}")
    print(f"Sum of odd numbers: {sum_of_odds}")
    print(f"Average of odd numbers: {average:.2f}")

except ValueError as e:
    print(f"Invalid input: {e}")
Last edited just now
