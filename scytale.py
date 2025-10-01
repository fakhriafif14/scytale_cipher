import math

# === Fungsi Enkripsi ===
def scytale_encrypt(text, key):
    if key <= 1:
        return text
    panjang = len(text)
    kolom = math.ceil(panjang / key)
    # Tambahkan padding agar panjang teks kelipatan key
    padded_text = text.ljust(kolom * key)
    result = []
    for i in range(0, key):  # loop baris
        j = i
        while j < len(padded_text):
            result.append(padded_text[j])
            j = j + key
    return "".join(result)


# === Fungsi Dekripsi ===
def scytale_decrypt(cipher, key):
    if key <= 1:
        return cipher
    panjang = len(cipher)
    kolom = math.ceil(panjang / key)
    # Bagi cipher menjadi baris-baris
    rows = []
    idx = 0
    for i in range(key):
        row_len = kolom
        # Baris terakhir bisa lebih pendek jika panjang tidak pas
        if idx + row_len > panjang:
            row_len = panjang - idx
        rows.append(cipher[idx:idx+row_len])
        idx += row_len
    # Baca per kolom
    result = []
    for i in range(kolom):
        for row in rows:
            if i < len(row):
                result.append(row[i])
    return "".join(result).rstrip()


# === Main Program ===
if __name__ == "__main__":
    plaintext = input("Masukkan teks yang akan dienkripsi: ")
    key = int(input("Masukkan key (jumlah baris): "))

    encrypted = scytale_encrypt(plaintext, key)
    decrypted = scytale_decrypt(encrypted, key)

    print("\n=== Hasil ===")
    print("Plaintext :", plaintext)
    print("Encrypted :", encrypted)
    print("Decrypted :", decrypted)
